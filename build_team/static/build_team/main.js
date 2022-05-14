document.addEventListener('DOMContentLoaded', function() {

    // listen for clicks
    document.addEventListener('click', event => {
        const element = event.target;
        // check if click was for add
        if (element.id ==='chosen') {
            console.log('add')
        } 

        // check if click was for remove
        if (element.id === 'poke_remove') {
            console.log('remove')
        }

    });
});

function poke_remove(elem) {
    const poke_id = elem.value
    const game = document.querySelector("#game").value;
        fetch(`/poke_remove`, {
            method:"POST",
            body: JSON.stringify({
            poke_id:poke_id,
            game:game
            })
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
        });
}


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