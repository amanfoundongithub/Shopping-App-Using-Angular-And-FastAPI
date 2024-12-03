import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

import axios from 'axios';


@Component({
  selector: 'app-navbar',
  imports: [CommonModule],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {

  username = ""
  profilePic = ""

  type = ""

  constructor(private router: Router) {
    const user_id = window.localStorage.getItem("id")
    if (user_id && this.username.length == 0) {
      axios.get("http://127.0.0.1:8000/user/fetch/" + user_id)
        .then((res) => {
          if (res.status == 200) {

            const data = res.data.user
            // this.orig_data = data


            this.username = data[1]

            // this.firstName = data[3]
            // this.lastName = data[4]

            // this.age = this.getAge(data[5])

            // this.gender = data[6]

            this.profilePic = data[7]

            this.type = data[8] 
            

            // this.dob = data[5]

          } else {

          }
        })
        .catch((err) => {
          console.log("AXIOS ERROR")
        })
    }
    else {
      this.router.navigate(["/login"])
    }

  }

  logOut() : void {
    if(window.localStorage.getItem("id")) {
      window.localStorage.removeItem("id")
      this.router.navigate(["/login"])
    }
    
  }

}
