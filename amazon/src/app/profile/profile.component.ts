import { Component } from '@angular/core';
import { NavbarComponent } from '../component/navbar/navbar.component';
import { CommonModule } from '@angular/common';

import axios from 'axios';

@Component({

  selector: 'app-profile',
  imports: [NavbarComponent, CommonModule],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})


export class ProfileComponent {


  orig_data = []

  items_list = []

  constructor() {
    const user_id = window.localStorage.getItem("id")
    console.log(this.username, user_id)
    if (user_id && this.username.length == 0) {
      axios.get("http://127.0.0.1:8000/user/fetch/" + user_id)
        .then((res) => {
          if (res.status == 200) {

            const data = res.data.user
            this.orig_data = data
            

            this.username = data[1]

            this.firstName = data[3]
            this.lastName = data[4]

            this.age = this.getAge(data[5])

            this.gender = data[6]

            this.profilePic = data[7]

            this.dob = data[5]

            this.type = data[8] 

            if(this.type == "seller") {
              axios.get("http://127.0.0.1:8000/item/find_by_seller/" + user_id)
              .then((res) => {
                if(res.status == 200) {
                  
                  const items = res.data.items 

                  this.items_list = items 
                
                }
                else {

                }
              })
              .catch((err) => {
                console.log(err) 
              })
            }

          } else {

          }
        })
        .catch((err) => {
          console.log("AXIOS ERROR")
        })
    }

  }

  getAge(dateString: string): Number {
    var today = new Date();
    var birthDate = new Date(dateString);
    var age = today.getFullYear() - birthDate.getFullYear();
    var m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }
    return age;
  }

  allow_edit_url = "fa-solid fa-pencil mt-4"
  disable_edit_url = "fa-solid fa-check mt-4"

  username = ""
  username_disabled = true

  firstName = ""
  firstname_disabled = true

  lastName = ""
  lastname_disabled = true

  age = this.getAge("2010-07-09")

  dob = ""

  gender = "Male"

  profilePic = "https://i.pinimg.com/originals/bc/27/6f/bc276ff73e30a5f50c493aeb685edb90.png"

  type = "customer"

  toggleEditUsername(): void {
    this.username_disabled = !this.username_disabled
  }

  editUserName(event: Event): void {
    let input = event.target as HTMLInputElement
    this.username = input.value
  }

  toggleEditFirstName() : void {
    this.firstname_disabled = !this.firstname_disabled
  }

  editFirstName(event : Event) : void {
    let input = event.target as HTMLInputElement
    this.firstName = input.value
  }

  toggleEditLastName() : void {
    this.lastname_disabled = !this.lastname_disabled
  }

  editLastName(event : Event) : void {
    let input = event.target as HTMLInputElement
    this.lastName = input.value
  }

  saveChanges() : void {
    axios.put("http://127.0.0.1:8000/user/update/" + window.localStorage.getItem("id"), {
      username: this.username,
      firstName: this.firstName,
      lastName: this.lastName,
      dob: this.dob,
      gender: this.gender,
      profilePic : this.profilePic,
    })
        .then((res) => {
          if (res.status == 200) {
            console.log(res.data)
            this.username_disabled = true
          } else {

          }
        })
        .catch((err) => {
          console.log("AXIOS ERROR")
        })
    }
  
  
  cancelChanges() : void {

  }

  profileFile : File | null = null 

  updateProfilePic(event : Event) : void {
    const input = event.target as HTMLInputElement 
    if(input.files && input.files[0]) {
      this.profileFile = input.files[0]
    }
  }

  saveProfilePic() : void {
    if (!this.profileFile) {
      alert("Please select a file to upload.");
      return;
    }

    let content = {
      "file" : this.profileFile
    }

    axios.post("http://127.0.0.1:8000/image/upload", content, {
      headers : {
        "Content-Type" : "multipart/form-data" 
      }
    })
    .then((res) => {
      if(res.status == 201) {
        this.profilePic = res.data.url 
      }
    })
    .catch((err) => {
      console.log(err) 
    })
  }

}
