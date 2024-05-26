const button1 = document.getElementById('button1');
const button2 = document.getElementById('button2');

const selfIntro = document.querySelector('selfIntro');
const sunsetIntro = document.querySelector('sunsetIntro');

// sunsetIntro를 숨기기
sunsetIntro.style.display = 'none';
selfIntro.style.display = 'none';

// button1 클릭 시 selfIntro를 보여줌/sunsetIntro를 숨김
button1.addEventListener('click', function() {
    selfIntro.style.display = 'block';
    sunsetIntro.style.display = 'none';
});

// button2 클릭 시 selfIntro를 숨김/ sunsetIntro를 보여줌
button2.addEventListener('click', function() {
    selfIntro.style.display = 'none';
    sunsetIntro.style.display = 'block';
});
