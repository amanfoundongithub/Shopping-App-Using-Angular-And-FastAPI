import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { Router } from '@angular/router';

import axios from 'axios';


@Component({
  selector: 'app-signup',
  imports: [CommonModule],
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.css'
})
export class SignupComponent {

  constructor(private router: Router) {
    if (window.localStorage.getItem("id")) {
      this.router.navigate(["/home"])
    }
  }



  firstName = ""
  classFirstName = "form-control"
  errorFirstName = ""
  setFirstName(event: Event): void {
    let input = event.target as HTMLInputElement
    this.firstName = input.value

    if (this.firstName.length == 0) {
      this.errorFirstName = "Given Name cannot be empty"
      this.classFirstName = "form-control is-invalid"
    }

    else {
      this.errorFirstName = ""
      this.classFirstName = "form-control is-valid"
    }
  }


  lastName = ""
  classLastName = "form-control"
  errorLastName = ""
  setLastName(event: Event): void {
    let input = event.target as HTMLInputElement
    this.lastName = input.value

    if (this.lastName.length == 0) {
      this.errorLastName = "Family Name cannot be empty"
      this.classLastName = "form-control is-invalid"
    }

    else {
      this.errorLastName = ""
      this.classLastName = "form-control is-valid"
    }
  }

  dob = "2000-12-10"
  classDOB = "form-control"
  errorDOB = ""
  setDOB(event: Event): void {
    let input = event.target as HTMLInputElement
    this.dob = input.value

    if (this.dob.length == 0) {
      this.errorDOB = "Date Of Birth cannot be empty"
      this.classDOB = "form-control is-invalid"
    }

    else {
      this.errorDOB = ""
      this.classDOB = "form-control is-valid"
    }
  }

  gender = ""
  classGender = "form-select"
  errorGender = ""
  setGender(event: Event): void {
    let input = event.target as HTMLInputElement
    this.gender = input.value

    if (this.gender.length == 0) {
      this.errorGender = "Please specify your gender!"
      this.classGender = "form-control is-invalid"
    }

    else {
      this.errorGender = ""
      this.classGender = "form-control is-valid"
    }
  }


  username = ""
  classUsername = "form-control"
  errorUserName = ""
  setUserName(event: Event): void {
    let input = event.target as HTMLInputElement
    this.username = input.value

    if (this.username.length == 0) {
      this.errorUserName = "Username cannot be empty"
      this.classUsername = "form-control is-invalid"
    }

    else {
      this.errorUserName = ""
      this.classUsername = "form-control is-valid"
    }
  }

  password = ""
  classPassword = "form-control"
  errorPassword = ""
  setPassword(event: Event): void {
    let input = event.target as HTMLInputElement
    this.password = input.value

    if (this.password.length < 8) {
      this.errorPassword = "Password is too short!"
      this.classPassword = "form-control is-invalid"
    }

    else {
      this.errorPassword = ""
      this.classPassword = "form-control is-valid"
    }
  }

  confirm_password = ""
  classConfirmPassword = "form-control"
  errorConfirmPassword = ""
  setConfirmPassword(event: Event): void {
    let input = event.target as HTMLInputElement
    this.confirm_password = input.value

    if (this.confirm_password != this.password) {
      this.errorConfirmPassword = "Password does not match!"
      this.classConfirmPassword = "form-control is-invalid"
    }

    else {
      this.errorConfirmPassword = ""
      this.classConfirmPassword = "form-control is-valid"
    }
  }

  type = "customer"
  classType = "form-control" 
  setType(event : Event) : void {
    let input = event.target as HTMLInputElement
    this.type = input.value 
  }
 

  agreed = false
  classAgreed = "form-check-input is-invalid"
  setAgreed(): void {
    this.agreed = !this.agreed

    if (this.agreed == false) {
      this.classAgreed = "form-check-input is-invalid"
    }
    else {
      this.classAgreed = "form-check-input is-valid"
    }
  }


  // Submit form
  loading = false
  submitDetails(): void {
    this.loading = true

    axios.post("http://127.0.0.1:8000/user/create", {
      username: this.username,
      password: this.password,
      firstName: this.firstName,
      lastName: this.lastName,
      dob: this.dob,
      gender: this.gender,
      type : this.type,
    }, {
      headers: { "Content-Type": "application/json" }
    })
      .then((res) => {
        if (res.status == 201) {
          alert('Successful Sign Up! Redirecting to Home Page...')
          window.localStorage.setItem("username", this.username)
          window.localStorage.setItem("password", this.password)
          window.localStorage.setItem("id", res.data.user)
          this.router.navigate(["/home"])
        
        }
      })
      .catch((err) => {
        alert(err)
        console.log(err)
      })
    return
  }
}
