import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import {Routes} from './routes'

export default () => 
    <div>
        <BrowserRouter>
                <Routes />
        </BrowserRouter>
        
    </div>

