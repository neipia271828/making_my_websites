let slideIndex = 0;
let slideInterval;
const slideDuration = 4500; // スライドの切り替え時間を設定（ミリ秒）
const buttonPadding = 40; // prev/next ボタンのパディング（左右合計）

window.onload = function() {
    const slides = document.querySelectorAll('.slide');
    const slider = document.querySelector('.slider');
    let maxHeight = 0; // スライドの最大高さを保存

    slides.forEach(slide => {
        const img = slide.querySelector('img');
        img.onload = function() {
            // 画像の幅に合わせてスライダーの幅を変更
            slider.style.width = img.width + 'px';

            // 画像の高さに合わせてスライダーの高さを更新
            if (img.height > maxHeight) {
                maxHeight = img.height;
                slider.style.height = maxHeight + 'px';
            }
        };
    });

    showSlides();
    slideInterval = setInterval(showSlides, slideDuration);
};

function showSlides() {
    const slides = document.getElementsByClassName("slide");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    slides[slideIndex - 1].style.display = "block";
}

function prevSlide() {
    clearInterval(slideInterval); // タイマーをクリア
    slideIndex -= 2;
    if (slideIndex < 0) { slideIndex = slides.length - 1 }
    showSlides();
    slideInterval = setInterval(showSlides, slideDuration); // タイマーを再設定
}

function nextSlide() {
    clearInterval(slideInterval); // タイマーをクリア
    showSlides();
    slideInterval = setInterval(showSlides, slideDuration); // タイマーを再設定
}