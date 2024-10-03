<script setup>
defineProps({
  navArray: [
    {
      label: String,
      url: String
    }
  ]
})
</script>

<template>
    <nav class="fixed flex justify-between py-6 w-full lg:px-48 md:px-12 px-4 content-center bg-secondary z-10">
    <div class="flex items-center">
      <img src='/assets/Logo_black.svg' alt="Logo" class="h-4" />
    </div>
    <ul class="font-montserrat items-center hidden md:flex">

      <li class="mx-3" v-for="navLink in navArray">
        <a class="growing-underline" href="navLink.url">
          {{ navLink.label }}
        </a>
      </li>
    </ul>
    <div id="showMenu" class="md:hidden cursor-pointer">
      <img src='/assets/logos/Menu.svg' alt="Menu icon" />
    </div>
  </nav>

  <div id='mobileNav' class="hidden px-4 py-6 fixed top-0 left-0 h-full w-full bg-secondary z-20 animate-fade-in-down">
    <div id="hideMenu" class="flex justify-end">
      <img src='/assets/logos/Cross.svg' alt="" class="cursor-pointer h-16 w-16" />
    </div>
    <ul class="font-montserrat flex flex-col mx-8 my-24 items-center text-3xl">
      
      <li class="my-6" v-for="navLink in navArray">
        <a href="navLink.url">
          {{ navLink.label }}
        </a>
      </li>
    </ul>
  </div>
</template>