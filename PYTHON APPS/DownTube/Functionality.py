import re
from tkinter.constants import END
import downtube as dt
import Exceptions as ex
from tkinter import messagebox as msg
from tkinter import filedialog as fd
import urllib.request
import pytube as pt
from pytube import YouTube


def clear(link, get_link):
    """ Clears the Entry box widget """
    download_link = link.get()
    if download_link == "":
        msg.showwarning(
                        title= "Warning",
                        message= "Warning: The input field is already empty",
                        )
    else :
        get_link.delete(0,last= len(download_link))

def browse_folder(get_dir):
    global dir_path
    dir_path = fd.askdirectory()
    get_dir.delete(0, END)
    get_dir.configure(fg= "black")
    get_dir.insert(0, dir_path)
    if dir_path == "":
        get_dir.configure(fg= "grey")
        get_dir.insert(0, "Choose a folder")

def check_connectivity(link):                   # Referred website: codespeedy (https://www.codespeedy.com/how-to-check-the-internet-connection-in-python/)
    """ Checks for internet connectivity or valid youtube link """
    try:
        urllib.request.urlopen(link)
    except:
        msg.showerror(
                    title= "Network Error",
                    message= "Connectivity issue found",
                    detail= "Check you internet connectivity \nor\n the link might not be correct"
                    )

def dwn(download_link, video_resolution, directory):
    """ Downloads the video """
    yt = pt.YouTube(download_link)
    try:
        if video_resolution == "":
           raise  ex.ResolutionError
    except ex.ResolutionError:
        msg.showerror(title= "Downtube",
                      message= "No video resolution found"
                      )
    if video_resolution == "360p":
        try:
            video = yt.streams.filter(progressive= True, file_extension= "mp4", res= "360p", type= "video").first()
            if video == None:
                raise AttributeError
            else:
                return video
                #video.download(output_path= directory)
        except AttributeError:
            msg.showinfo(title= "Downtube",
                         message= "The video resolution is not available to be downloaded ",
                         detail= "Try downloading with other resolution"
                        )
    elif video_resolution == "720p":
        try:
            video = yt.streams.filter(progressive= True, file_extension= "mp4", res= "720p", type= "video").first()
            if video == None:
                raise AttributeError
            else:
                return video
            #video.download(output_path= directory)
        except AttributeError:
            msg.showinfo(title= "Downtube",
                         message= "The video resolution is not available to be downloaded ",
                         detail= "Try downloading with other resolution"
                        )

def clear_inputs(get_link, get_resolution):
    input_of_get_link = get_link.get()
    input_of_get_resolution = get_resolution.get()
    get_link.delete(0,last= len(input_of_get_link))
    get_resolution.delete(0,last= len(input_of_get_resolution))



def download_bt(download_link, get_link, video_resolution, directory, get_dir, resolution_box ):
    """ All the process for downloading will be done here """
    verify_YT = re.search(r"youtube.com", download_link)   # Verifying youtube link or not


    try:
        """ Checks for youtube link and rasie error if link is not valid or not found """
        if download_link == "":
            raise ex.Link_Error
        elif verify_YT == None:
            raise ex.InvalidLink
        else:
            check_connectivity(download_link)
            get_link.delete(0,last= len(download_link))
            try:
                if directory == "":
                    raise ex.DirectoryError
                else:
                    vid = dwn(download_link, video_resolution, directory)
                    vid.download(directory) #type: ignore
                    clear_inputs(get_dir, resolution_box)
            except ex.DirectoryError:
                msg.showerror(title= "Directory error",
                              message= "Directory Error: No Directory is found",
                              detail= "Browse or enter the directory to save the file"
                              )
    except ex.Link_Error:
        msg.showerror(
                    title= "Link Error",
                    message= "Youtube link Not Found",
                    detail= "You've not given any link in the \"Link section\""
                    )
    except ex.InvalidLink:
        msg.showerror(
                    title= "Invalid link",
                    message= "Error: Invalid link",
                    detail= "The given link is invalid or doesn't belongs to youtube"
                    )

    try:
        if directory == "Choose a folder" :
            raise ex.DirectoryError
    except ex.DirectoryError:
        msg.showerror(
                    title = "Directory Error",
                    message="Error: No directory is given to save the file"
                    )

if __name__=='__main__':
    dt.main()
