import { Routes } from '@angular/router';
import { SignupComponent } from './auth/signup/signup.component';
import { HomeComponent } from './home/home.component';
import { ErrorComponent } from './error/error.component';
import { ProfileComponent } from './profile/profile.component';
import { LoginComponent } from './auth/login/login.component';
import { AdditemComponent } from './additem/additem.component'; 


export const routes: Routes = [
    {
        path: 'register',
        component: SignupComponent

    },
    {
        path: 'home',
        component: HomeComponent

    },
    {
        path: 'profile',
        component: ProfileComponent,

    },
    {
        path: 'login', 
        component: LoginComponent 
    },
    {
        path : 'additem',
        component : AdditemComponent
    },
    {
        path: '**',
        component: ErrorComponent
    },
];

