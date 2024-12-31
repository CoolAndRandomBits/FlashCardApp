let currentCard = 0;
const notecards = document.querySelectorAll('.notecard');
const cardCounter = document.getElementById('card-counter');

notecards.forEach((card, index) => {
    card.addEventListener('click', () => {
        card.style.transform = card.style.transform === 'rotateY(180deg)' ? 'rotateY(0deg)' : 'rotateY(180deg)';
    });
});

function showCard(index) {
    notecards.forEach((card, i) => {
        card.style.display = i === index ? 'block' : 'none';
    });
    updateCounter();
}

function prevCard() {
    currentCard = (currentCard === 0) ? notecards.length - 1 : currentCard - 1;
    showCard(currentCard);
}

function nextCard() {
    currentCard = (currentCard === notecards.length - 1) ? 0 : currentCard + 1;
    showCard(currentCard);
}

function updateCounter() {
    cardCounter.textContent = `${currentCard + 1}/${notecards.length}`;
}

showCard(currentCard);
