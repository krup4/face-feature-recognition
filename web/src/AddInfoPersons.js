const videoPlayerZone = document.getElementById('videoPlayerZone');

const createBoundingBox = (ind, x1, y1, x2, y2, cw, ch) => {
    const boundingBox = document.createElement('div');
    boundingBox.id = ind + 'bbox';
    boundingBox.onmouseenter = openInfoZone;
    boundingBox.onmouseleave = closeInfoZone;
    boundingBox.classList.add('bounding-box');
    let norml;
    if (cw > ch) {
        norml = videoPlayer.offsetWidth / cw;
    } else {
        norml = videoPlayer.offsetHeight / ch;
    }
    const normX1 = x1 * norml + (videoPlayer.offsetWidth - cw * norml) / 2;
    const normY1 = y1 * norml + (videoPlayer.offsetHeight - ch * norml) / 2;
    const normX2 = (x2 - x1) * norml;
    const normY2 = (y2 - y1) * norml;
    boundingBox.style.left = normX1 + 'px';
    boundingBox.style.top = normY1 + 'px';
    boundingBox.style.width = Math.min(normX2, videoPlayer.offsetWidth) + 'px';
    boundingBox.style.height = Math.min(normY2, videoPlayer.offsetHeight) + 'px';
    videoPlayerZone.appendChild(boundingBox);
}

const createInfoZone = (ind, age, gender, emotion) => {
    const infoZone = document.createElement('div');
    infoZone.id = ind + 'ibox';
    infoZone.classList.add('info-box');
    infoZone.classList.add('fade-out');
    infoZone.classList.add('hide');
    infoZone.innerText += `Возраст: ${age}\nПол: ${gender}\nЭмоция: ${emotion}`;
    infoZone.style.top = '50px';
    infoZone.style.left = '5px';
    videoPlayerZone.appendChild(infoZone)
}

const openInfoZone = (e) => {
    const ind = e.target.id.slice(0, -4);
    const infoZone = document.getElementById(ind + 'ibox');
    infoZone.classList.remove('hide')
}

const closeInfoZone = (e) => {
    const ind = e.target.id.slice(0, -4);
    const infoZone = document.getElementById(ind + 'ibox');
    infoZone.classList.add('hide')
}

