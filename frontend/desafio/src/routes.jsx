import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import Home from './pages/Home'
import Detalhes from './pages/DetalhesCartao'
import Lista from './pages/ListaCartoes'
import Confirmacao from './pages/Confirmacao'
import SolicitarCartao from './pages/SolicitarCartao'

export const Routes = () => {
    return (
      <Switch>
        <Route path='/' component={Home} exact />
        <Route path='/lista' component={Lista} />
        <Route path='/detalhes' component={Detalhes} />
        <Route path='/confirmacao' component={Confirmacao} />
        <Route path='/solicitar' component={SolicitarCartao} />
      </Switch>
      )
    }

