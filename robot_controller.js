import React from 'react';
import { View, StyleSheet, TouchableOpacity, Text } from 'react-native';

class RobotController extends React.Component {
  move_forward = () => {
    console.log('Enviando comando para frente...');
    // código para enviar o comando para frente
  }

  move_backward = () => {
    console.log('Enviando comando para trás...');
    // código para enviar o comando para trás
  }

  move_left = () => {
    console.log('Enviando comando para a esquerda...');
    // código para enviar o comando para a esquerda
  }

  move_right = () => {
    console.log('Enviando comando para a direita...');
    // código para enviar o comando para a direita
  }

  render() {
    return (
      <View style={styles.container}>
        <TouchableOpacity style={styles.button} onPress={this.move_forward}>
          <Text style={styles.text}>Frente</Text>
        </TouchableOpacity>
        <View style={styles.row}>
          <TouchableOpacity style={styles.button} onPress={this.move_left}>
            <Text style={styles.text}>Esquerda</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={this.move_right}>
            <Text style={styles.text}>Direita</Text>
          </TouchableOpacity>
        </View>
        <TouchableOpacity style={styles.button} onPress={this.move_backward}>
          <Text style={styles.text}>Trás</Text>
        </TouchableOpacity>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f5fcff',
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    width: '80%',
  },
  button: {
    backgroundColor: '#2196f3',
    borderRadius: 10,
    padding: 10,
    marginVertical: 10,
    minWidth: 100,
    alignItems: 'center',
  },
  text: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 18,
  },
});

export default RobotController;
