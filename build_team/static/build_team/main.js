document.addEventListener('DOMContentLoaded', function() {

    // listen for clicks
    document.addEventListener('click', event => {
        const element = event.target;

        // check if click was for search
        if (element.id ==='chosen') {
            console.log('add')
        }
    });
});


// function poke_add() {
//     console.log('add2')
//     const pokemon = document.querySelector("#pokemon_chosen").value;
//     const game = document.querySelector("#games").value;
//     fetch(`/poke_add/`, {
//         method:"POST",
//         body: JSON.stringify({
//         pokemon:pokemon,
//         game:game
//         })
//     })
//     .then(response => response.json())
//     .then(result => {
//         console.log(result);
//     });
// }