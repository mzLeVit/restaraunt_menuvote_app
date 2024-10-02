document.getElementById("backButton").addEventListener("click", function() {
    window.history.back(); // Simulates going back to the previous page
});

document.getElementById("changeVoteButton").addEventListener("click", function() {
    alert("Redirecting to vote page...");
    window.location.href = 'vote.html';
});


// Simulated vote data (you can replace this with actual data)
const totalVotes = 0; // Change this value to test the behavior

window.onload = function() {
    if (totalVotes === 0) {
        // Hide the results section and total votes
        document.getElementById("resultsSection").style.display = "none";
        document.getElementById("totalVotes").style.display = "none";
        
        // Show the no votes message
        document.getElementById("noVotesMessage").style.display = "block";
    } else {
        // Show the results and total votes
        document.getElementById("resultsSection").style.display = "block";
        document.getElementById("totalVotes").style.display = "block";
        
        // Hide the no votes message
        document.getElementById("noVotesMessage").style.display = "none";
    }
};
