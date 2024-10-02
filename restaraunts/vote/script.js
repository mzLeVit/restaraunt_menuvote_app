document.getElementById('backButton').addEventListener('click', function() {
    window.history.back();
});

document.getElementById('lunchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const selectedLunch = document.querySelector('input[name="lunch"]:checked').value;
    
    alert(`You voted for: ${selectedLunch.replace('_', ' ')}`);
});
