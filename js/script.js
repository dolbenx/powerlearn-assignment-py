// Navigation: Switch active planet
const navLinks = document.querySelectorAll('.nav-link');
const sections = document.querySelectorAll('.planet-section');

navLinks.forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const planet = link.getAttribute('data-planet');

    // Update active nav link
    navLinks.forEach(l => l.classList.remove('active'));
    link.classList.add('active');

    // Show corresponding section
    sections.forEach(section => {
      if (section.id === planet) {
        section.classList.add('active');
      } else {
        section.classList.remove('active');
      }
    });

    // Trigger skill bar animation if on About section
    if (planet === 'about') {
      animateSkillBars();
    }
  });
});

// Skill Bar Animation
function animateSkillBars() {
  const bars = document.querySelectorAll('.skill-bar');
  bars.forEach(bar => {
    const width = bar.getAttribute('data-width');
    bar.style.width = '0'; // Reset
    setTimeout(() => {
      bar.style.width = `${width}%`; // Animate to full width
    }, 100);
  });
}

// Form Submission
const form = document.getElementById('contact-form');
const formMessage = document.getElementById('form-message');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const message = document.getElementById('message').value;

  if (name && email && message) {
    formMessage.textContent = 'Message sent! (Simulated)';
    formMessage.style.color = '#00d4ff';
    form.reset();
    setTimeout(() => formMessage.textContent = '', 3000);
  } else {
    formMessage.textContent = 'Please fill all fields.';
    formMessage.style.color = '#ff4d4d';
  }
});

// Initial skill bar animation on load if About is active
if (document.querySelector('#about.active')) {
  animateSkillBars();
}

// Generate twinkling stars dynamically
document.addEventListener("DOMContentLoaded", function () {
  const spaceBg = document.querySelector(".space-bg");

  for (let i = 0; i < 100; i++) {
      const star = document.createElement("div");
      star.className = "star";
      star.style.top = `${Math.random() * 100}vh`;
      star.style.left = `${Math.random() * 100}vw`;
      star.style.animationDelay = `${Math.random() * 5}s`;
      spaceBg.appendChild(star);
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const spaceBg = document.querySelector(".space-bg");

  // Create Moon
  const moon = document.createElement("div");
  moon.className = "moon";
  spaceBg.appendChild(moon);
});