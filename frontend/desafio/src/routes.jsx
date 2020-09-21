import React from 'react'
import { BrowserRouter, Switch, Route, Redirect } from 'react-router-dom'
import Home from './pages/Home'
import Detalhes from './pages/DetalhesCartao'
import Lista from './pages/ListaCartoes'
import SolicitarCartao from './pages/SolicitarCartao'

export const Routes = () => {
    return (
      <Switch>
        <Redirect exact from="/" to="/lista" />
        {/*<Route path='/' component={Home} exact />*/}
        <Route path='/lista' component={Lista} />
        <Route path='/detalhes' component={Detalhes} />
        <Route path='/solicitar' component={SolicitarCartao} />
        <Redirect exact from="/" to="/lista" />
      </Switch>
      )
    }

