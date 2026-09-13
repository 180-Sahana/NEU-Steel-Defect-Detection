import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.set_page_config(
    page_title="NEU Steel Defect Detection",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 NEU Steel Surface Defect Detection")
st.write("Upload a steel-surface image to detect defects using YOLO.")

model = YOLO("runs/detect/results/neu_yolo_safe/weights/best.pt")

uploaded_file = st.file_uploader(
    "Upload a steel-surface image",
    type=["jpg", "jpeg", "png"]
)

# Defect severity information
severity_info = {
    "scratches": {
        "severity": "Medium",
        "risk": "Surface damage"
    },
    "rolled-in_scale": {
        "severity": "High",
        "risk": "Surface quality degradation"
    },
    "pitted_surface": {
        "severity": "High",
        "risk": "Material surface damage"
    },
    "patches": {
        "severity": "Medium",
        "risk": "Surface quality degradation"
    },
    "inclusion": {
        "severity": "High",
        "risk": "Internal material impurity"
    },
    "crazing": {
        "severity": "High",
        "risk": "Surface cracking"
    }
}

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Uploaded Image")
    st.image(image, width="stretch")

    if st.button("Detect Defects"):

        results = model.predict(
            image,
            imgsz=512,
            conf=0.25,
            verbose=False
        )

        result_image = results[0].plot()

        st.subheader("Detection Result")
        st.image(result_image, width="stretch")

        boxes = results[0].boxes

        if len(boxes) == 0:
            st.warning("No defect detected.")

        else:
            st.success(f"{len(boxes)} defect(s) detected.")

            st.subheader("Defect Analysis")

            for box in boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                class_name = model.names[class_id]

                info = severity_info.get(
                    class_name,
                    {
                        "severity": "Unknown",
                        "risk": "Unknown"
                    }
                )

                st.write(
                    f"### 🔍 {class_name}"
                )

                st.write(
                    f"**Confidence:** {confidence:.2%}"
                )

                st.write(
                    f"**Severity:** {info['severity']}"
                )

                st.write(
                    f"**Risk:** {info['risk']}"
                )

                st.divider()