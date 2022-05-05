
// document.addEventListener('DOMContentLoaded', function() {

//     // listen for clicks
//     document.addEventListener('click', event => {
//         const element = event.target;

//         // check if click was to edit the team
//         if (element.id ==='edit_team') {
//             console.log('success')
//         }

//         // check if click was for search
//         if (element.id ==='poke_search') {
//             const search = document.querySelector("#searched").value;
//             poke_search(search)
//         }
//     });
// });


// probably not going to use this 

// function poke_search(pokemon) {
//     fetch(`/poke_search/${pokemon}`, {
//         method:"GET",
//     })
//     .then(response => response.json())
//     .then(result => {
//         console.log(result);
//     });
// }