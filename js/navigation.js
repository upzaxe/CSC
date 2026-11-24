// Navigasi mobile
const navToggle=document.querySelector('.nav-toggle'),links=document.querySelector('.links');if(navToggle && links){navToggle.addEventListener('click',()=>{const open=links.classList.toggle('open');navToggle.setAttribute('aria-expanded',String(open));navToggle.setAttribute('aria-label',open?'Tutup menu':'Buka menu');});links.addEventListener('click',e=>{if(e.target.closest('a')){links.classList.remove('open');navToggle.setAttribute('aria-expanded','false');}});}
// Menampilkan header setelah scroll

const header = document.querySelector('.nav');

function updateHeader() {
    if (window.scrollY > 100) {
        header.classList.add('visible');
    } else {
        header.classList.remove('visible');
    }
}

window.addEventListener('scroll', updateHeader, {
    passive: true
});

updateHeader();
