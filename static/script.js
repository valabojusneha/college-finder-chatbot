function filterColleges() {
    let rank = document.getElementById("rank").value;
    let branch = document.getElementById("branch").value;

    fetch("/filter", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            rank: rank,
            branch: branch
        })
    })
    .then(response => response.json())
    .then(data => {
        let output = document.getElementById("results");
        output.innerHTML = "";

        if (data.length === 0) {
            output.innerHTML = "<p>No colleges found</p>";
            return;
        }

        data.forEach(college => {
            output.innerHTML += `
                <div class="card">
                    <h3>${college.name}</h3>
                    <p>Branch: ${college.branch}</p>
                    <p>Cutoff: ${college.cutoff_rank}</p>
                    <p>Fees: ${college.fees}</p>
                    <p>Location: ${college.location}</p>
                </div>
            `;
        });
    });
}