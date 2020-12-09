function init()
{
    // block to position the card "holders"
    let cards = document.getElementsByClassName('card-container');
    let emShift = 9.5;
    for(let i = 1; i < cards.length; i++)
    {
        let old = Number(cards[i-1].style.left.split('em')[0]);
        if(i >= 5)
        {
            if(i == 5)
            {
                old = (-emShift) + Number(cards[0].style.left.split('em')[0]);
            }
            
            cards[i].style.top = "20em";
        }
        cards[i].style.left = `${old + emShift}em`;
    }

    request("POST", "init", null, (ev) => {
        // parse the response as JSON
        let res = ev.response;
        let gameData = JSON.parse(res);
        console.log(gameData)

        // Update screen
        update_output(gameData);
        

        // setOutput(JSON.stringify(gameData))
    });

}

function update_output(data)
{
    if(data.master)
    {
        setTimeout(() => {
            let playAgain = confirm(`${data.master} Would you like to play again?`);
            if(playAgain)
            {
                window.location.reload();
            }
            else
            {

            }
        }, 1000)
        
    }

    let dealerCards = data.dealer.cards;
    let playerCards = data.player.cards;
    drawCards(dealerCards, playerCards);

    // draw the count of the cards known
    document.getElementById('pCount').innerText = `Player: ( ${data.player.count} )`;
    document.getElementById('dCount').innerText = `Dealer: ( ${data.dealer.count} )`;

    
}

function drawCards(dealerCards, playerCards)
{
    for(let i = 0; i < dealerCards.length; i++)
    {
        document.getElementById(`d${i}`).children[0].innerText = dealerCards[i];
    }
    for(let i = 0; i < playerCards.length; i++)
    {
        document.getElementById(`p${i}`).children[0].innerText = playerCards[i];
    }
}

function onHit()
{
    request("GET", "hit", null, (ev) => {
        let res = ev.response;
        let gameData = JSON.parse(res);
        console.log(gameData)

        update_output(gameData);
    });
}

function onStand()
{
    request("GET", "stand", null, (ev) => {
        let res = ev.response;
        let gameData = JSON.parse(res);
        console.log(gameData)

        update_output(gameData);
    });
}

function setOutput(data)
{
    document.getElementById('debug').innerHTML = data;
}

function request(method, endpoint, data=null, cb=((ev) => {}))
{
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) 
        {
            let self = this;
            cb(self);
        }
    };
    xhttp.open(method, endpoint, true);
    xhttp.send(data);
}