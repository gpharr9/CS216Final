function init()
{
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
        let res = ev.response;
        console.log(res);
    })

}

function onHit()
{
    request("GET", "hit", null, (ev) => {
        let res = ev.response;
        setOutput(res);
    });
}

function onStand()
{
    request("GET", "stand", null, (ev) => {
        let res = ev.response;
        setOutput(res);
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