<script lang="ts">
	import type { PhotoSwipeEntityImage } from '$lib/components/ui/ImageGridGallery.svelte';
	import ImageGridGallery from '$lib/components/ui/ImageGridGallery.svelte';
	import Title from '$lib/components/ui/Title.svelte';

	let imgs: PhotoSwipeEntityImage[] = [
		{
			src: './gallery/Gallery (40).jpg',
			width: 4032,
			height: 3024
		},
		{
			src: './gallery/Gallery (20).JPG',
			width: 2592,
			height: 1944
		},
		{
			src: './gallery/Gallery (4).jpeg',
			width: 900,
			height: 1600
		},
		{
			src: './gallery/Gallery (41).jpg',
			width: 4032,
			height: 3024
		},
		{
			src: './gallery/Gallery (14).JPG',
			width: 2592,
			height: 1944
		},
		{
			src: './gallery/Gallery (45).jpeg',
			width: 1500,
			height: 2000
		},
		{
			src: './gallery/Gallery (25).jpg',
			width: 4000,
			height: 3000
		},
		{
			src: './gallery/Gallery (31).jpg',
			width: 4000,
			height: 3000
		},
		{
			src: './gallery/Gallery (11).jpeg',
			width: 900,
			height: 1600
		},
		{
			src: './gallery/Gallery (7).jpg',
			width: 4032,
			height: 3024
		},
		{
			src: './gallery/Gallery (32).jpg',
			width: 4032,
			height: 3024
		},
		{
			src: './gallery/Gallery (5).jpg',
			width: 1080,
			height: 810
		},
		{
			src: './gallery/Gallery (8).jpg',
			width: 3024,
			height: 4032
		},
		{
			src: './gallery/Gallery (11).jpg',
			width: 4032,
			height: 3024
		},
		{
			src: './gallery/Gallery (43).jpeg',
			width: 1500,
			height: 2000
		},
		{
			src: './gallery/Gallery (42).jpeg',
			width: 1500,
			height: 2000
		},
		{
			src: './gallery/Gallery (16).JPG',
			width: 2592,
			height: 1944
		},
		{
			src: './gallery/Gallery (8).jpeg',
			width: 1600,
			height: 900
		},
		{
			src: './gallery/Gallery (2).jpeg',
			width: 1600,
			height: 900
		},
		{
			src: './gallery/Gallery (9).jpg',
			width: 4000,
			height: 3000
		},
		{
			src: './gallery/Gallery (37).jpg',
			width: 4000,
			height: 3000
		},
		{
			src: './gallery/Gallery (17).JPG',
			width: 1944,
			height: 2592
		},
		{
			src: './gallery/Gallery (15).JPG',
			width: 2592,
			height: 1944
		},
		{
			src: './gallery/Gallery (10).jpeg',
			width: 900,
			height: 1600
		},
		{
			src: './gallery/Gallery (24).jpg',
			width: 4032,
			height: 3024
		},
		{
			src: './gallery/Gallery (7).jpeg',
			width: 900,
			height: 1600
		},
		{
			src: './gallery/Gallery (22).jpg',
			width: 4032,
			height: 3024
		},
		{
			src: './gallery/Gallery (27).JPG',
			width: 2592,
			height: 1944
		},
		{
			src: './gallery/Gallery (30).jpg',
			width: 4000,
			height: 3000
		},
		{
			src: './gallery/Gallery (10).jpg',
			width: 4000,
			height: 3000
		},
		{
			src: './gallery/Gallery (6).jpeg',
			width: 1600,
			height: 900
		},
		{
			src: './gallery/Gallery (13).JPG',
			width: 2592,
			height: 1944
		},
		{
			src: './gallery/Gallery (44).jpeg',
			width: 1500,
			height: 2000
		},
		{
			src: './gallery/Gallery (12).JPG',
			width: 2592,
			height: 1944
		},
		{
			src: './gallery/Gallery (3).jpeg',
			width: 900,
			height: 1600
		},
		{
			src: './gallery/Gallery (36).jpg',
			width: 4000,
			height: 3000
		},
		{
			src: './gallery/Gallery (12).jpeg',
			width: 900,
			height: 1600
		},
		{
			src: './gallery/Gallery (18).JPG',
			width: 2592,
			height: 1944
		},
		{
			src: './gallery/Gallery (28).jpg',
			width: 4000,
			height: 3000
		},
		{
			src: './gallery/Gallery (21).JPG',
			width: 2592,
			height: 1944
		},
		{
			src: './gallery/Gallery (23).jpg',
			width: 4032,
			height: 3024
		},
		{
			src: './gallery/Gallery (33).jpg',
			width: 4000,
			height: 3000
		},
		{
			src: './gallery/Gallery (26).jpg',
			width: 4032,
			height: 3024
		},
		{
			src: './gallery/Gallery (29).jpg',
			width: 4032,
			height: 3024
		},
		{
			src: './gallery/Gallery (1).jpeg',
			width: 900,
			height: 1600
		},
		{
			src: './gallery/Gallery (1).jpg',
			width: 1836,
			height: 3264
		},
		{
			src: './gallery/Gallery (9).jpeg',
			width: 900,
			height: 1600
		},
		{
			src: './gallery/Gallery (3).jpg',
			width: 3264,
			height: 1836
		},
		{
			src: './gallery/Gallery (34).jpg',
			width: 4032,
			height: 3024
		},
		{
			src: './gallery/Gallery (5).jpeg',
			width: 900,
			height: 1600
		},
		{
			src: './gallery/Gallery (38).jpg',
			width: 4000,
			height: 3000
		},
		{
			src: './gallery/Gallery (2).jpg',
			width: 3264,
			height: 1836
		},
		{
			src: './gallery/Gallery (6).jpg',
			width: 4032,
			height: 3024
		},
		{
			src: './gallery/Gallery (4).jpg',
			width: 4032,
			height: 3024
		},
		{
			src: './gallery/Gallery (35).jpg',
			width: 4000,
			height: 3000
		},
		{
			src: './gallery/Gallery (19).JPG',
			width: 2592,
			height: 1944
		},
		{
			src: './gallery/Gallery (39).jpg',
			width: 4000,
			height: 3000
		}
	];
</script>

<Title>Galleria</Title>

<section>
	<ImageGridGallery {imgs} />
</section>
