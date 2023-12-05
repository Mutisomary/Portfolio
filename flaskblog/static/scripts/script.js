const welcomeText = document.getElementById('welcome-text');
const content = document.getElementById('content');

// Function to reveal text letter by letter
function revealText(element) {
  element.classList.remove('hidden');
  const text = element.textContent;
  element.textContent = '';
  
  for (let i = 0; i < text.length; i++) {
    setTimeout(() => {
      element.textContent += text[i];
    }, 100 * i);
  }
}

// Reveal the "Welcome to Science Spot" text
revealText(welcomeText);

// Display content after text reveal
setTimeout(() => {
  content.classList.remove('hidden');
}, 100 * welcomeText.textContent.length);