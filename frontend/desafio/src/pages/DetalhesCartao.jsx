import React, { Component } from 'react'
import Titulo from '../components/Titulo'
import axios from 'axios'

class SolicitacaoDetalhes extends Component {
    constructor(props){
        super(props)
        this.stage = {
            dados:null
        }
    }

    componentDidMount(id){

        const url= "htto://127.0.0.1/solicitacoes/" + id
        axios.get(url)
        .then((response) => {
            let aux = JSON.stringify(response.data).parse()
            this.setState({ dados:aux })
            }
        )
    }

    //getDados(){
//
    //}
}

export default () =>  (
    <>
    <Titulo titulo = 'Detalhes' />
    </>
)