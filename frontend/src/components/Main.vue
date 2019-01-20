<template>
  <div class="flex-row top-aligned">
      <div class="textcontainer">
          <Input placeholder="Enter title"/>
          <EditorWindow placeholder="Start writing your awesome story.."/>
      </div>
	  <div class="sidebar">
		  <div class="suggestion-box" :class="{'category-selected':this.selectedCategory!=null}">
			  <h3>Trending categories</h3>
			  <ul>
				<li v-for="cat in topCategories" class="suggestion"> 
					<a href="#" @click="selectCategory(cat.id)"	>{{cat.id}} </a>
				</li>
			  </ul>
		  </div>

		  <div v-if="selectedCategory!=null" class="suggestion-box" >
			  <h3>Popular times for {{selectedCategory}}</h3>
			  <ul>
				<li v-for="cat in categoryTimes" v-if="selectedCategory==cat.id" class="suggestion"> 
					{{formatTs(cat.popularTimestamp)}}
				</li>
			  </ul>
		  </div>

		  <div v-if="selectedCategory!=null" class="suggestion-box" >
			  <h3>Expected user interest in {{selectedCategory}}</h3>
			  <ul>
				<li v-for="cat in readPercentages" v-if="selectedCategory==cat.id" class="suggestion"> 
				  <div class="line" :style='{top: 10 * cat.totalBlocks}' > </div>
					{{round(cat.readPercentage)}}%
				</li>
			  </ul>
		  </div>
	  </div>
  </div>
</template>

<script>
import Input from './Input.vue'
import EditorWindow from './EditorWindow.vue'
import { db } from '../utils/firebase.js'

export default {
    name: 'Main',
    props: {
        msg: String
    },
    components: {
        Input,
		EditorWindow
    },
	data: () => ({
		selectedCategory: null,
		topCategories: [],
		categoryTimes: [],
		readPercentages: []
	}),
	firestore: ()=>({
		topCategories: db.collection('topCategories'),
		categoryTimes: db.collection('categoryTimes'),
		readPercentages: db.collection('readPercentages')
	}),
	methods:{
		selectCategory(cat){
			this.selectedCategory = cat;
		},
		formatTs(ts){
			return (new Date(ts)).toLocaleTimeString();
		},
		round(num){
			return Math.round(num*100)/100;
		}
	}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.textcontainer {
    width: 70%;
    margin: 10px auto;
    display: flex;
    flex-direction: column;
}

.line{
	position: absolute;
    height: 5px;
    background: lightblue;
    width: 10%;
    top: 600px;
    left: 0;
}

.suggestion-box.category-selected {
    height: 0;
	width: 0;
    padding: 0;
    margin: 0;
    transition: 0.4s all;
	overflow: hidden;
}

input:focus, #article:focus{
	outline: none;
}

#article{
	text-align: left;
}

ul{
	list-style: none;
    text-align: left;
}

input {
    width: 60%;
    font-size: 3rem;
    margin: 0px 0px 40px 0;
}

.suggestion-box{
	background: limegreen;
    padding: 20px;
    color: white;
    margin-right: 40px;
    margin-bottom: 20px;
	a{
		color: white;
		text-decoration: none;
		font-weight: bold;
		cursor: pointer;
		&:hover{
			text-decoration: underline;
		}
	}
}


.sidebar{
	width: 25%;
}

.content-editor.empty:before {
		margin-top: 1em;
        display: block;
        position: absolute;
		opacity: 0.5;
        content: attr(data-placeholder);
	}
</style>
