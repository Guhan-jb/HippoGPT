// --------------
// Hover animaton
// --------------

const mouthSpeed = 0.3;
const easeType = Power2.easeOut;
const mouthOpen = gsap.timeline({ paused: true });
mouthOpen.to('.mouth-back', {duration: mouthSpeed, ease: easeType, y: -70}, 0);
mouthOpen.to('.tongue', {duration: mouthSpeed * 1.5, ease: easeType, y: -70}, 0);
mouthOpen.to('.teeth', {duration: mouthSpeed, ease: easeType, y: -70, scaleY: 1.2}, 0);
mouthOpen.to('.body', {duration: mouthSpeed, ease: easeType, scaleY: 1.06, transformOrigin: 'center bottom'}, 0);
mouthOpen.to('.freckles', {duration: mouthSpeed, ease: easeType, y: -10}, 0);
mouthOpen.to('.ears', {duration: mouthSpeed, ease: easeType, y: 6}, 0);
mouthOpen.to('.eye-right', {duration: mouthSpeed, ease: easeType, x: -2}, 0);
mouthOpen.to('.eye-left', {duration: mouthSpeed, ease: easeType, x: 2}, 0);
mouthOpen.to('.eyes', {duration: mouthSpeed, ease: easeType, y: 2}, 0);
mouthOpen.to('.nostrils', {duration: mouthSpeed, ease: easeType, y: -6}, 0);

// ------------
// Mouse events
// ------------

const button = document.querySelector('button');

button.addEventListener('mouseenter', enterButton);
button.addEventListener('mouseleave', leaveButton);

function enterButton() { mouthOpen.play(); }
function leaveButton() { mouthOpen.reverse(); }

// ----------
// Ear wiggle
// ----------

const earWiggle = gsap.timeline({ paused: true, repeat: 2 });
earWiggle.set('.ear-right', { transformOrigin:"center center" });
earWiggle.to('.ear-right', {duration: 0.1, rotation: 45});
earWiggle.to('.ear-right', {duration: 0.1, rotation: 0});

window.setInterval(() => earWiggle.play(0), 2500);

// ------------
// Eye tracking
// ------------

const eyeRightPupil = document.querySelector('.eye-right-pupil');
const eyeLeftPupil = document.querySelector('.eye-left-pupil');
const eyeLeftInner = document.querySelector('.eye-left-inner');
const innerEyeWidth = eyeLeftInner.getBoundingClientRect().width;
const innerEyeHeight = eyeLeftInner.getBoundingClientRect().height;
const pupilWidth = eyeLeftPupil.getBoundingClientRect().width;
const pupilHeight = eyeLeftPupil.getBoundingClientRect().height;
const xMovement = (innerEyeWidth - pupilWidth)/2;
const yMovement = (innerEyeHeight - pupilHeight)/2;

window.addEventListener('mousemove', updateEyePosition);

function updateEyePosition(e) {
  const mousePercentX = e.clientX / document.body.clientWidth;
  const mousePercentY = e.clientY / document.body.clientHeight;
  const posX = (mousePercentX * 2 - 1) * xMovement;
  const posY = (mousePercentY * 2 - 1) * yMovement;

  eyeLeftPupil.style.transform = `translate(${posX}px, ${posY}px)`;
  eyeRightPupil.style.transform = `translate(${posX}px, ${posY}px)`;
}

particlesJS("particles-js", {
  particles: {
    number: { value: 50, density: { enable: true, value_area: 800 } },
    color: { value: "#ffffff" },
    shape: {
      type: "circle",
      stroke: { width: 0, color: "#000000" },
      polygon: { nb_sides: 5 },
      image: { src: "img/github.svg", width: 100, height: 100 },
    },
    opacity: {
      value: 0.5,
      random: false,
      anim: { enable: false, speed: 1, opacity_min: 0.1, sync: false },
    },
    size: {
      value: 3,
      random: true,
      anim: { enable: false, speed: 40, size_min: 0.1, sync: false },
    },
    line_linked: {
      enable: true,
      distance: 150,
      color: "#ffffff",
      opacity: 0.4,
      width: 1,
    },
    move: {
      enable: true,
      speed: 6,
      direction: "none",
      random: false,
      straight: false,
      out_mode: "out",
      bounce: false,
      attract: { enable: false, rotateX: 600, rotateY: 1200 },
    },
  },
  interactivity: {
    detect_on: "canvas",
    events: {
      onhover: { enable: false, mode: "grab" },
      onclick: { enable: true, mode: "repulse" },
      resize: true,
    },
    modes: {
      grab: { distance: 400, line_linked: { opacity: 1 } },
      bubble: { distance: 400, size: 40, duration: 2, opacity: 8, speed: 3 },
      repulse: { distance: 200, duration: 0.4 },
      push: { particles_nb: 4 },
      remove: { particles_nb: 2 },
    },
  },
  retina_detect: true,
});
