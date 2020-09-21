import React from 'react'
import Titulo from '../components/Titulo'
import axios from 'axios'
import { Redirect } from 'react-router-dom'
import {TextField, Button} from '@material-ui/core'
import {Container, Box} from '@material-ui/core'
import BotaoVolar from '../components/BotaoVoltar'

class SolicitacaoCartaoForm extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            dados: {
                nome:"",
                data_nascimento:"",
                rg:"",
                cpf:"",
                telefone:"",
                email:"",
                renda:"",
            },
            path_redirect:"/lista",
            salvo_flag:false
        }

        this.handleInputChange = this.handleInputChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handleInputChange(event){
        const target = event.target
        const value =  target.value
        const name = target.name

        const dados = { ...this.state.dados };
        dados[name] = value
        
        this.setState({
            dados
        })
    }
    
    handleSubmit(event){
        event.preventDefault();
        console.log(this.state);
        let resp;
        resp = this.salvarDados();
        console.log(resp);
        
    }

    salvarDados(){

        // salva a flag como true para redirecioar para a tela de lsitagem

        let url = 'http://127.0.0.1:9090/solicitacoes'
        axios.post(url, this.state.dados)
            .then((response) => {
                alert("salvo com sucesso");
                this.setState({
                    salvo_flag:true
                })
            })
    }

    render(){

        if (this.state.salvo_flag) {
            return <Redirect to={this.state.path_redirect} />
        }

        return (
            <form onSubmit={this.handleSubmit} >
                <TextField
                 label="Nome"
                 id="outlined-margin-none"
                 variant="outlined"
                 name="nome"
                 value={this.state.nome} onChange={this.handleInputChange} />
                <br />

                <TextField
                  label="Data de nascimento"
                  type="date"
                  variant="outlined"
                  defaultValue="2017-05-24"
                  name="data_nascimento"
                  value={this.state.data_nascimento} onChange={this.handleInputChange}
                />
                <br />

                <TextField
                 label="RG"
                 id="outlined-margin-none"
                 variant="outlined"
                 name="rg"
                 value={this.state.rg} onChange={this.handleInputChange}
                 />
                 <br />

                <TextField
                 label="CPF"
                 id="outlined-margin-none"
                 variant="outlined"
                 name="cpf"
                 value={this.state.cpf} onChange={this.handleInputChange}/>
                 <br />

                <TextField
                 label="Telefone"
                 id="outlined-margin-none"
                 variant="outlined"
                 name="telefone"
                 value={this.state.telefone} onChange={this.handleInputChange}/>
                 <br />
            
                <TextField
                 label="Renda"
                 id="outlined-margin-none"
                 variant="outlined"
                 name="renda"
                 value={this.state.renda} onChange={this.handleInputChange}/>
                 <br />

                <TextField
                 label="Email"
                 id="outlined-margin-none"
                 variant="outlined"
                 name="email"
                 value={this.state.email} onChange={this.handleInputChange}/>
                 <br />
                 <Box display="flex" justifyContent='flex-end'p={1}>
                     <Box flexGrow={1}>
                      <Button variant='contained' color='primary' type="submit"> Salvar </Button>
                     </Box>
                     <Box p={1}>
                        <BotaoVolar />
                     </Box>    
                </Box>
                

            </form>
        )
    }

}

export default () =>  (
    <>
    <Container maxWidth='sm'>
      <Titulo titulo = 'Nova solicitação de cartão' />
      <SolicitacaoCartaoForm />
    </Container>
    </>
)