document.addEventListener('DOMContentLoaded', function() {

    // check for gym container
    const gym_container = document.querySelector('.gym_container')
    if (gym_container) {
        document.querySelectorAll('.leader_box').forEach( function(leader) {
            leader.onmouseover = () => {
                const color = leader.querySelector('.leader_color');
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

    // check for team container
    const teams_container = document.querySelector('.teams_container')
    if (teams_container) {
        document.querySelectorAll('.teams_link').forEach( function(team) {
            team.onmouseover = () => {
                const color = team.querySelector('.team_color');
                const hex = color.innerHTML
                const red = parseInt(hex[1]+hex[2],16);
                const green = parseInt(hex[3]+hex[4],16);
                const blue = parseInt(hex[5]+hex[6],16);
                team.style.backgroundColor = `rgba(${red},${green},${blue},.4)`
            }
            team.onmouseout = () => {
                team.style.backgroundColor = '';   
            }
        })

    }
});