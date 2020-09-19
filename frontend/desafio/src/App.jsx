import React from 'react'
//import Lista from './components/Lista'
import Titulo from './components/Titulo'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import Home from './pages/Home'
import Detalhes from './pages/DetalhesCartao'
import Lista from './pages/ListaCartoes'
import {Routes} from './routes'
import Menu from './components/Menu'

export default () => 
    <div>
        {/* <Titulo titulo='Todas' />
        <Titulo titulo='Todos os cartoes' /> */}
        <BrowserRouter>
            <Menu />
            <Routes />
        </BrowserRouter>
        
    </div>

