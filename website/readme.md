### here is my websites materials

#### flask highlights
- append more than static folders

```python
from flask import send_from_directory
'''
from flask import Flask
app = Flask(__name__)
# the comment code is in another file
'''
@app.route('/movies/<path:filename>')
def custom_static(filename):
    return send_from_directory('/media/disk2/spurs/movie/movies', filename)
```

> then go the http:ip:port/movies/filename to visit.

- solving flask crashing when using matplotlib
> RuntimeError: main thread is not in main loop with Matplotlib and Flask. 
Tkinter isn't thread safe, and the general consensus is that Tkinter doesn't work in a non-main thread. 
If you rewrite your code so that Tkinter runs in the main thread, you can have your workers run in other threads.
The main caveat is that the workers cannot interact with the Tkinter widgets. They will have to write data to a queue, and your main GUI thread will have to poll that queue.

```python
import matplotlib
matplotlib.use('Agg')
```

- saving figure to base64 and send to frontend(html)
```python
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from io import BytesIO
import base64

def plot_im(fpaths): #fpaths = {'en' : path_to_english_audio, 'ch' : path_to_chinese_audio}
    titles = {'en':['en_mel-gram', 'en_spectrogram'], 'ch':['ch_mel-gram', 'ch_spectrogram']}
    keys = ['en', 'ch']
    ret = {}
    for i, k in enumerate(keys):
        fig = plt.figure()
        mel = get_spectrograms(fpaths[k])

        im = plt.imshow(mel, aspect='auto')
        #fig.subplots_adjust(left=0.07, bottom=0.05, right=0.9, top=0.92, wspace=0.18, hspace=0.30)
        cbar_ax = fig.add_axes([0.92, 0.05, 0.025, 0.87])
        fig.colorbar(im, cax=cbar_ax)
        #plt.title(titles[k][0], loc='center')

        save_file = BytesIO()
        plt.savefig(save_file, format='png')
        file_base64 = base64.b64encode(save_file.getvalue()).decode('utf-8')
        ret[k+'_mel'] = file_base64
        plt.close() # high importantly

    return ret

```

> as we using 'utf-8' to encode the image, so we deal in the following codes in html (flask return ret (json.dumps), ret={'en_mel': mel_base64, 'ch_mel': mel_base64}

``` js
/*
ret = eval("(" + ret + ")")
*/
var img = document.createElement('img');
img.src = 'data:image/png;charset=utf-8;base64, ' + res['en_mel'];
var td = document.createElement('td');
td.appendChild(img);

```

#### html table hightlight

- add border

```html
<table border="8" cellspacing="10">
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
</table>
```

- insert row and its columns.

```js
res = eval("(" + res + ")"); // res is the ajax response, success: function(res){}
var tbody = document.getElementById('tbody');

var row = tbody.insertRow(0);

var h2 = document.createElement('h2');
h2.textContent = input + ': ' + 'ch_melspectrogram'
var td = document.createElement('td');
td.appendChild(h2);
row.appendChild(td);

var img = document.createElement('img');
img.src = 'data:image/png;charset=utf-8;base64, ' + res['ch_mel']
var td = document.createElement('td');
td.appendChild(img);
row.appendChild(td);


var td = document.createElement('td');
var audio = document.createElement('audio');
audio.setAttribute('controls', '');
var wav = document.createElement('source');
wav.src = res['ch'];
audio.appendChild(wav);
td.appendChild(audio);
row.appendChild(td);

var td = document.createElement('td');
var txt = document.createElement('h4');
txt.textContent = res['ch_txt'];
td.appendChild(txt);
row.appendChild(td);

```

- remove items from table

```js
function clear_wav(){
    tbody = document.getElementById('tbody');
    while(true){
        if (tbody.rows.length > 0){
            tbody.deleteRow(0);
        }
        else{
            break;
        }
    }
    /*
    var container = document.getElementById('wav');
    while(true){
        var p = container.getElementsByTagName('p');
        if (p.length > 0){
            container.removeChild(p[0]);
        }
        else{
            break;
        }
    }
    */
}
```

#### js regular match
```js
var reg = /^[0-9]{4}$/ ; # start with digit and end with digit and the total length is four and all characters are digital.
var astr = "222a"
reg.test(astr) # return false

var reg = /^[0-9]+$/ ; # all are digital.
var reg= /^[A-Za-z]+$/; # all are english characters.

```
