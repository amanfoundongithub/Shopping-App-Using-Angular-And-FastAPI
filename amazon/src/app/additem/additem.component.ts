import { Component } from '@angular/core';
import { NavbarComponent } from '../component/navbar/navbar.component';
import { FormsModule } from '@angular/forms';

import axios from 'axios';

@Component({
  selector: 'app-additem',
  imports: [NavbarComponent, FormsModule],
  templateUrl: './additem.component.html',
  styleUrl: './additem.component.css'
})
export class AdditemComponent {

  itemName = ""
  
  itemCode = ""

  itemQuantity = ""

  itemPrice = 0.0

  itemType = ""

  itemDescription = ""

  itemSeller = window.localStorage.getItem("id") 

  createItem() {
    const newItem = {
      itemName: this.itemName,
      itemCode: this.itemCode,
      itemQuantity: this.itemQuantity,
      itemPrice: this.itemPrice,
      itemType: this.itemType,
      itemDescription: this.itemDescription,
      itemSeller: this.itemSeller
    };

    axios.post('http://localhost:8000/item/create', newItem)
      .then(response => {
        console.log('Item created successfully:', response.data);
        alert('Item created successfully!');
      })
      .catch(error => {
        console.error('Error creating item:', error);
        alert('Failed to create item. Please try again.');
      });
  }

  
}
