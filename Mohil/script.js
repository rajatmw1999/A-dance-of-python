function validate(){
    
    var ff = document.querySelector(".name");
    var gg = document.querySelector(".phone");
    var hh = document.querySelector(".email");
    
    var nameValue = ff.value;
    var phoneValue = gg.value;
    var emailValue = hh.value;
    
    var nameRegularExp = /^[A-Za-z]+$/;
    var phoneRegularExp = /^[789]\d{9}$/;
    var emailRegularExp = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    var nameError = document.querySelector(".nameError")
    var phoneError = document.querySelector(".phoneError")
    var emailError = document.querySelector(".emailError")

    function disappear(){
        nameError.innerHTML = " "
        phoneError.innerHTML = " "
        emailError.innerHTML = " "
    }

    if(nameRegularExp.test(nameValue)){
        console.log("Found")
    }
    else{
        console.log("not found")
        nameError.innerHTML = "Invalid Name"
        setTimeout(disappear, 5000)
    }


    if(phoneRegularExp.test(phoneValue)){
        console.log("Found")
    }
    else{
        console.log("not found")
        phoneError.innerHTML = "Invalid Contact Number"
        setTimeout(disappear, 5000)
    }


    if(emailRegularExp.test(emailValue)){
        console.log("Found")
    }
    else{
        console.log("not found")
        emailError.innerHTML = "Invalid Email"
        setTimeout(disappear, 5000)
    }
    
    
    
}