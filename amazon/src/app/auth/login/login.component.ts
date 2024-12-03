import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {Router} from '@angular/router';
import axios from 'axios';

@Component({
  selector: 'app-login',
  imports: [CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

    constructor(private router : Router) {
      if (window.localStorage.getItem("id")) {
        this.router.navigate(["/home"])
      }
    }

    username = ""
    password = ""

    errorEmail = ""
    errorPassword = ""

    classEmail = "form-control"
    classPassword = "form-control"

    updateEmail(event : Event) : void {
      const input = event.target as HTMLInputElement
      this.username = input.value 

      if(this.validateEmail() == false) {
        this.classEmail = "form-control is-invalid"
      }
      else {
        this.classEmail = "form-control is-valid" 
      }
    }

    updatePassword(event : Event) : void {
      const input = event.target as HTMLInputElement
      this.password = input.value 
      
      if(this.validatePassword() == false) { 
        this.classPassword = "form-control is-invalid"
      }
      else {
        this.classPassword = "form-control is-valid"
      }
    }

    validatePassword() : boolean {
      if(this.password.length < 8) {
        this.errorPassword = "Password should contain at least 8 characters"
        return false
      }

      return true
    }

    validateEmail() : boolean {
      return true 
    }

    // Submit form
  loading = false
  submitDetails(): void {
    this.loading = true

    axios.post("http://127.0.0.1:8000/user/authenticate", {
      username: this.username,
      password: this.password,
    }, {
      headers: { "Content-Type": "application/json" }
    })
      .then((res) => {
        if (res.status == 200) {
          if(res.data.verified){
            alert('Successful Login! Redirecting to Home Page...')
            window.localStorage.setItem("username", this.username)
            window.localStorage.setItem("id", res.data.id)
            this.router.navigate(["/home"])
          }
          else {
            alert("Failed to login")
          }
          
          
        }
      })
      .catch((err) => {
        alert(err)
        console.log(err)
      })
    return
  }
}
