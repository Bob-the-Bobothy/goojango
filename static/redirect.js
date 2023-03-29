document.addEventListener('DOMContentLoaded', () => {
  const redirectButton = document.getElementById('redirect');
  const googleButton = document.getElementById('google');
  const shrekButton = document.getElementById('shrek');

  redirectButton.addEventListener('click', () => {
    window.location.href = '/';
  });
  googleButton.addEventListener('click', () => {
    window.location.href = 'https://google.com';
  })
  shrekButton.addEventListener('click', () => {
    window.location.href = 'https://google.com/search?q=shrek'
  })
});