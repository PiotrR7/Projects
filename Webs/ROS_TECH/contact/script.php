<?php
    if (isset($_POST['submit'])) {
        if (isset($_POST['first-name']) && isset($_POST['last-name']) && isset($_POST['mail']) && isset($_POST['phone-number']) && isset($_POST['message'])) {
            $con = mysqli_connect("localhost", "root", "", "rostech");
            
            $first_name = mysqli_real_escape_string($con, $_POST['first-name']);
            $last_name = mysqli_real_escape_string($con, $_POST['last-name']);
            $mail = mysqli_real_escape_string($con, $_POST['mail']);
            $phone_number = mysqli_real_escape_string($con, $_POST['phone-number']);
            $message = mysqli_real_escape_string($con, $_POST['message']);  
        
    
            // Database connect
            $x = "INSERT INTO messages (`id`, `first_name`, `last_name`, `e-mail`, `phone_number`, `message`, `date`) 
            VALUES (NULL, '$first_name', '$last_name', '$mail', '$phone_number', '$message', NOW());";
            $query = mysqli_query($con, $x);
    
            // Check if query was successful
            if($query) {
                header('Location: contact/succes.html');
            } else {
                header('Location: contact/error.html');
            }
            
            mysqli_close($con);
            exit();
        }
    }
?>