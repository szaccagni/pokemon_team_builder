document.addEventListener('DOMContentLoaded', function() {

    // check for gym container
    const gym_container = document.querySelector('.gym_container')
    if (gym_container) {
        document.querySelectorAll('.leader_box').forEach( function(leader) {
            leader.onmouseover = () => {
                const color = leader.querySelector('.leader_color');
                console.log(color.innerHTML);
                leader.style.backgroundColor = color.innerHTML;
            }
            leader.onmouseout = () => {
                leader.style.backgroundColor = '';   
            }
        })
    } 

    // check for gym_info section
    const gym_info = document.querySelector('.gym_info'); 
    if (gym_info) {
        gym_info.style.backgroundColor = gym_info.dataset.color;
    }
});