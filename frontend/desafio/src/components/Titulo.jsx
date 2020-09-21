import React from'react'
import {Box} from '@material-ui/core'

export default (props) => (
    <Box display="flex" justifyContent='center' border={1} borderRadius={16} bgcolor="success.main"
      width="100%" mb={2}>
    <h2> {props.titulo} </h2>
    </Box>

)
