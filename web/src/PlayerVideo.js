const people = document.getElementById("people")
const engagement = document.getElementById("engagement")
const genders = document.getElementById("genders")
const mage = document.getElementById("mage")

let cntSendFrame = 0;

const sendFrame = (frameDataURL, cw, ch) => {
    const url = "http://127.0.0.1:8080/api/getInfo";

    const blob = dataURLToBlob(frameDataURL);

    const formData = new FormData();
    formData.append("image", blob, "frame.jpg");

    ++cntSendFrame;
    fetch(url, {
        method: "POST",
        body: formData,
    })
        .then((response) => {
            if (response.ok) {
                console.log("Кадр успешно отправлен!");
                --cntSendFrame;
                return response.json();
            } else {
                console.error("Ошибка отправки кадра!");
            }
        })
        .then((json) => {
            if (!cntSendFrame) {
                const data = JSON.parse(atob(json));
                let p = 0;
                let i = 0;
                let k = 0;
                let sAge = 0;
                let m = 0, f = 0;
                let e = 0;
                const goodE = ['сердитая', 'отвращение',
                    'страх', 'счастливая', 'грустная', 'удивления'];
                for (const box of data) {
                    if (box['name'] == "face") {
                        createBoundingBox(i, box['boxes'][0], box['boxes'][1], box['boxes'][2], box['boxes'][3], cw, ch);
                        createInfoZone(i, box['age'], box['gender'], box['emotion']);
                        sAge += parseFloat(box['age']);
                        if (box['gender'] == 'М') ++m;
                        else ++f;
                        if (goodE.includes(box['emotion'])) ++e;
                        ++k;
                    } else {
                        ++p;
                    }
                    ++i;
                }
                if (p) {
                    people.innerText = p;
                    engagement.innerText = e / p * 100 + "%";
                }
                if (k) {
                    genders.innerText = m + ' М, ' + f + ' Ж';
                    mage.innerText = sAge / k;
                }
            }
        })
        .catch((error) => {
            console.error("Ошибка при выполнении запроса:", error);
        });
}

const dataURLToBlob = (dataURL) => {
    const byteString = atob(dataURL.split(",")[1]);
    const mimeString = dataURL.split(",")[0].split(":")[1].split(";")[0];
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
    }
    return new Blob([ab], { type: mimeString });
}

const videoStop = () => {
    const canvas = document.createElement("canvas");
    canvas.width = videoPlayer.videoWidth;
    canvas.height = videoPlayer.videoHeight;

    const ctx = canvas.getContext("2d");
    ctx.drawImage(videoPlayer, 0, 0, canvas.width, canvas.height);

    const dataURL = canvas.toDataURL("image/jpeg");

    sendFrame(dataURL, canvas.width, canvas.height);
};

const videoPlay = () => {
    const children = videoPlayerZone.querySelectorAll('div');
    children.forEach(child => videoPlayerZone.removeChild(child));
    engagement.innerText = '';
    genders.innerText = '';
    mage.innerText = '';
}