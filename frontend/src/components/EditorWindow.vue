<template>
	  <div :data-placeholder="placeholder" id="article" ></div>
</template>

<script>
export default {
	name: 'Input',
	props: {
	  placeholder: String
	},
    mounted(){
		const config = {
			setup:function(editor){
				editor.on('init', function () {
					// Default classes of tinyMCE are a bit weird
					// I add my own class on init
					// this also sets the empty class on the editor on init
					tinymce.DOM.addClass( editor.bodyElement, 'content-editor empty' );
				});

				// You CAN do it on 'change' event, but tinyMCE sets debouncing on that event
				// so for a tiny moment you would see the placeholder text and the text you you typed in the editor
				// the selectionchange event happens a lot more and with no debouncing, so in some situations
				// you might have to go back to the change event instead.
				 editor.on('selectionchange', function () {
					 if ( editor.getContent() === "" ) {
						 tinymce.DOM.addClass( editor.bodyElement, 'empty' );
					 } else {
						 tinymce.DOM.removeClass( editor.bodyElement, 'empty' );
					 }
				 });
			},
			selector: '#article',
			menubar: false,
			inline: true,
			theme: 'inlite',
			insert_toolbar: '',
			selection_toolbar: 'bold italic underline',
		  };
        tinymce.init(config);
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	input {
		border: none;
	}
	input:focus {
		border: none;
	}
</style>
