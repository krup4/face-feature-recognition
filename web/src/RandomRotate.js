const logo = document.querySelector('.main-logo');
const randomAngle = () => Math.floor(Math.random() * 360);
const randomSign = () => Math.random() > 0.5 ? 1 : -1;

logo.style.setProperty('--random-angle', `${randomAngle() * randomSign()}deg`);

setInterval(() => {
    logo.style.setProperty('--random-angle', `${randomAngle() * randomSign()}deg`);
}, 7000);