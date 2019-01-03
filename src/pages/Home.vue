<template>
  <main-layout>
  	<div id="logoDiv" >
      <div style="position: absolute;left: 1%;right:1%;filter:alpha(opacity=50)" align="center" class="backgroundDiv">
        <img id="logoImg" src="/logo.jpg" style="z-index: 10;width: auto;height: 89vh;"  alt="Logo" />
      </div>
   </div>
   
 </main-layout>
</template>

<script>
  import $ from "../jquery.min.js"
  class Particle{
    constructor(canvas, options){
      let colors = ["#feea00","#a9df85","#5dc0ad", "#ff9a00","#fa3f20"]
      let types  = ["full","fill","empty"]
      this.random = Math.random()
      this.progress = 0;
      this.x = ($(window).width()/2)  + (Math.random()*200 - Math.random()*200)
      this.y = ($(window).height()/2) + (Math.random()*200 - Math.random()*200)
      this.w = $(window).width()
      this.h = $(window).height()
      this.radius = 1 + (8*this.random)
      this.type  = types[this.randomIntFromInterval(0,types.length-1)];
      this.color = colors[this.randomIntFromInterval(0,colors.length-1)];
      this.a = 0
      this.s = (this.radius + (Math.random() * 1))/10;
      //this.s = 12 //Math.random() * 1;
    }
    setCanvas(tCanvas){
      this.canvas = tCanvas;
      console.log("setCanvas",tCanvas)
    }
    getCoordinates(){
      return {
        x: this.x,
        y: this.y
      }
    }

    randomIntFromInterval(min,max){
      return Math.floor(Math.random()*(max-min+1)+min);
    }

    render(){
      // Create arc
      let lineWidth = 0.2 + (2.8*this.random);
      let color = this.color;
      switch(this.type){
        case "full":
        this.createArcFill(this.radius, color)
        this.createArcEmpty(this.radius+lineWidth, lineWidth/2, color)
        break;
        case "fill":
        this.createArcFill(this.radius, color)
        break;
        case "empty":
        this.createArcEmpty(this.radius, lineWidth, color)
        break;
      }
    }

    createArcFill(radius, color){
      this.canvas.beginPath();
      this.canvas.arc(this.x, this.y, radius, 0, 2 * Math.PI);
      this.canvas.fillStyle = color;
      this.canvas.fill();
      this.canvas.closePath();
    }

    createArcEmpty(radius, lineWidth, color){
      this.canvas.beginPath();
      this.canvas.arc(this.x, this.y, radius, 0, 2 * Math.PI);
      this.canvas.lineWidth = lineWidth;
      this.canvas.strokeStyle = color;
      this.canvas.stroke();
      this.canvas.closePath();
    }

    move(){

      this.x += Math.cos(this.a) * this.s;
      this.y += Math.sin(this.a) * this.s;
      this.a += Math.random() * 0.4 - 0.2;

      if(this.x < 0 || this.x > this.w - this.radius){
        return false
      }

      if(this.y < 0 || this.y > this.h - this.radius){
        return false
      }
      this.render()
      return true
    }

    calculateDistance(v1, v2){
      let x = Math.abs(v1.x - v2.x);
      let y = Math.abs(v1.y - v2.y);
      return Math.sqrt((x * x) + (y * y));
    }
  }

  import MainLayout from '../layouts/Main.vue'

  export default {
    components: {
      MainLayout
    },
    data(){
      return {
        frequency:100,
        max_particles:100,
        particles:[],
        init_num:this.max_particles,
        max_time:this.frequency*this.max_particles,
        time_to_recreate:false,
        canvas:undefined,
      }
    },
    mounted:function(){
      this.tela = document.createElement('canvas');
      this.tela.width = $(window).width();
      this.tela.height = $("#logoImg").height();
      console.log($("#logoImg").height())
      $("#logoDiv").append(this.tela);

      this.canvas = this.tela.getContext('2d');

    // Enable repopolate
    setTimeout(function(){
      this.time_to_recreate = true;
    }.bind(this), this.max_time)

    // Popolate particles
    this.popolate(this.max_particles);

    
    this.update()
  },
  methods:
  {
    /*
 * Function to clear layer canvas
 * @num:number number of particles
 */
 updateParticels(){
  var tParticle = new Particle(this.canvas)
  tParticle.setCanvas(this.canvas)
  this.particles.push(tParticle)
  console.log(this.canvas)
 },
 popolate(num){
  for (var i = 0; i < num; i++) {
   setTimeout(this.updateParticels(),this.frequency*i);
 }
 return this.particles.length
},

clear(){
  this.canvas.fillStyle='#111111';
  this.canvas.fillRect(0, 0, this.tela.width, this.tela.height);
},
connection(){
  this.old_element = null
  for(let element in this.particles) {  
    element = this.particles[element]
    let box1 = element.getCoordinates()
    if (this.old_element != null)
    {box1= this.old_element.getCoordinates()}
    let box2 = element.getCoordinates()
    this.canvas.beginPath();
    this.canvas.moveTo(box1.x,box1.y);
    this.canvas.lineTo(box2.x,box2.y);
    this.canvas.lineWidth = 0.45;
    this.canvas.strokeStyle="#3f47ff";
    this.canvas.stroke();
    this.canvas.closePath(); 
    this.old_element = element
  };

},
 update(){
  this.clear();
  this.connection()
  this.particles = this.particles.filter(function(p) { return p.move() })
  if(this.time_to_recreate){
    if(this.particles.length < this.init_num){ popolate(1);}
  }
  requestAnimationFrame(this.update.bind(this))
}
}
}
</script>
