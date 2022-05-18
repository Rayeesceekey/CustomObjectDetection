import json
import shutil
from pathlib import Path
import numpy as np
from tqdm import tqdm


def make_dirs(dir='converted_yolo/'):
    dir = Path(dir)
    if dir.exists():
        shutil.rmtree(dir)
    for p in dir, dir / 'annotations':
        p.mkdir(parents=True, exist_ok=True)
    return dir

def convert_coco_json(json_dir):
    save_dir = make_dirs()  # output directory

    for json_file in sorted(Path(json_dir).resolve().glob('*.json')):
        fn = Path(save_dir) / 'annotations'
        with open(json_file) as f:
            data = json.load(f)

        images = {'%g' % x['id']: x for x in data['images']}

        for x in tqdm(data['annotations'], desc=f'Annotations {json_file}'):
            if x['iscrowd']:
                continue

            img = images['%g' % x['image_id']]
            h, w, f = img['height'], img['width'], img['file_name']

            # The COCO box format is [top left x, top left y, width, height]
            box = np.array(x['bbox'], dtype=np.float64)
            box[:2] += box[2:] / 2  # xy top-left corner to center
            box[[0, 2]] /= w  # normalize x
            box[[1, 3]] /= h  # normalize y

            # Write
            if box[2] > 0 and box[3] > 0: 
                cls = x['category_id']
                line = cls, *(box)
                with open((fn / f).with_suffix('.txt'), 'a') as file:
                    file.write(('%g ' * len(line)).rstrip() % line + '\n')


if __name__ == '__main__':
    convert_coco_json('trainval/annotations')  # directory with *.json