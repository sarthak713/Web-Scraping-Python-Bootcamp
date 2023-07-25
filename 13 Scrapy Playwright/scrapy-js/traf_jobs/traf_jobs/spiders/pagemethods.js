const interval_id=setImmediate(function(){
    const button=document.querySelector("#results > div.py-3.ng-star-inserted > button")
    if(button){
        button.scrollIntoView()
        button.click()
    }
    else{
        clearInterval(interval_id)
    }
}, 1000)