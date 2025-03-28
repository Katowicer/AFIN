<script lang="ts">
	import type { PhotoSwipeEntityImage } from '$lib/components/ui/ImageGridGallery.svelte';
	import ImageGridGallery from '$lib/components/ui/ImageGridGallery.svelte';
	import Title from '$lib/components/ui/Title.svelte';

	let imgs: PhotoSwipeEntityImage[] = [
		{
			src: 'https://cdn.pixabay.com/photo/2019/10/17/14/52/kitten-4557097_1280.jpg',
			width: 800,
			height: 600
		},
		{
			src: 'https://cdn.pixabay.com/photo/2018/05/04/16/50/cat-3374422_1280.jpg',
			width: 800,
			height: 600
		},
		{
			src: 'https://cdn.pixabay.com/photo/2015/11/16/14/43/cat-1045782_1280.jpg',
			width: 800,
			height: 600
		},
		{
			src: 'https://cdn.pixabay.com/photo/2018/01/03/19/17/cat-3059075_1280.jpg',
			width: 800,
			height: 600
		},
		{
			src: 'https://images.pexels.com/photos/57416/cat-sweet-kitty-animals-57416.jpeg?auto=compress&cs=tinysrgb&w=600',
			width: 800,
			height: 600
		},
		{
			src: 'https://images.pexels.com/photos/1543793/pexels-photo-1543793.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
			width: 800,
			height: 600
		}
	];
</script>

<Title>Galleria</Title>

<section>
	<ImageGridGallery {imgs} />
</section>
