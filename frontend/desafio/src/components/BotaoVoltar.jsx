import React from 'react'
import {Button} from '@material-ui/core'
import {Link} from 'react-router-dom'

export default (props) => {
    return (
      <Button variant='contained' component={Link} to="/lista" color='primary' > Voltar para lista </Button>
    )
    }