<template>
    <input type="text" value="" name="" id="" :placeholder="placeholder"/>
</template>

<script>
export default {
  name: 'Input',
  props: {
    placeholder: String
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
