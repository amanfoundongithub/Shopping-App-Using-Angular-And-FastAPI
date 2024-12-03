import { Component } from '@angular/core';
import { NavbarComponent } from '../component/navbar/navbar.component';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  imports: [NavbarComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {


}
