const btn = document.querySelector('.btn-menu');
const nav = document.querySelector('nav');
const brn = document.querySelector('.brightness');

btn.addEventListener('click', () => {
  nav.classList.toggle('open-menu')
　brn.classList.toggle('open-menu2')
  // if (btn.innerHTML === 'メニュー') {
  //   btn.innerHTML = '閉じる';
  // } else {
  //   btn.innerHTML = 'メニュー';
  // }
  // ↑ これと同じ意味の三項演算子での書き方 ↓{% static 'menu.png' %}
  btn.innerHTML = btn.innerHTML === '<div align="right"><div class="button008 navdiv"><a class="navdiv" href="#"><p class="navp">------</p></a></div></div>'
    ? '<div align="right"><div class="button008 navdiv"><a class="navdiv" href="#"><p class="navp"><<<<</p></a></div></div>'
    : '<div align="right"><div class="button008 navdiv"><a class="navdiv" href="#"><p class="navp">------</p></a></div></div>'
});
