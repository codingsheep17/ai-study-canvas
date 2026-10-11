
import {ReflexEvent,applyEventActions,isTrue,mergeSlotProps,refs} from "$/utils/state"
import {StateContexts,UploadFilesContext,addEvents} from "$/utils/context"
import {Fragment,memo,useCallback,useContext,useEffect,useRef} from "react"
import {jsx} from "@emotion/react"
import {Box as RadixThemesBox,Button as RadixThemesButton,Flex as RadixThemesFlex,Text as RadixThemesText} from "@radix-ui/themes"
import {} from "react-dropzone"
import {useDropzone} from "react-dropzone"
import LucideUpload from "lucide-react/dist/esm/icons/upload.mjs"
import LucideImage from "lucide-react/dist/esm/icons/image.mjs"
import LucideCheck from "lucide-react/dist/esm/icons/check.mjs"
import LucideDot from "lucide-react/dist/esm/icons/dot.mjs"








export const Cond_comp_263b2a94c85b5278add1d81edbc73bf3_b314f0b3 = /*#__PURE__*/ (() => {
const Cond_comp_263b2a94c85b5278add1d81edbc73bf3_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        ((reflex___state____state__ai_study_canvas___home____state.level_rx_state_?.valueOf?.() === "School student"?.valueOf?.())?(children?.at?.(0)):(children?.at?.(1)))
    )
});
Cond_comp_263b2a94c85b5278add1d81edbc73bf3_b314f0b3.displayName = "Cond";
return Cond_comp_263b2a94c85b5278add1d81edbc73bf3_b314f0b3;
})();

export const Box_box_b2648d643be7668769c362a7ec5d891a_b314f0b3 = /*#__PURE__*/ (() => {
const Box_box_b2648d643be7668769c362a7ec5d891a_b314f0b3 = memo(({children, ...rest}) => {
    const on_click_4607b90ad20f51b03776e9e1ee877621 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ai_study_canvas___home____state.set_level", ({ ["value"] : "School student" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])
const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        jsx(RadixThemesBox,{...mergeSlotProps(rest, ({ css:({ ["cursor"] : "pointer", ["padding"] : "1rem 1.25rem", ["borderRadius"] : "12px", ["border"] : ((reflex___state____state__ai_study_canvas___home____state.level_rx_state_?.valueOf?.() === "School student"?.valueOf?.()) ? "1px solid #6366F1" : "1px solid rgba(255,255,255,0.08)"), ["background"] : ((reflex___state____state__ai_study_canvas___home____state.level_rx_state_?.valueOf?.() === "School student"?.valueOf?.()) ? "#6366F126" : "transparent"), ["boxShadow"] : ((reflex___state____state__ai_study_canvas___home____state.level_rx_state_?.valueOf?.() === "School student"?.valueOf?.()) ? "0 0 24px #6366F133" : "none"), ["width"] : "100%" }), onClick:on_click_4607b90ad20f51b03776e9e1ee877621 }))},children)
    )
});
Box_box_b2648d643be7668769c362a7ec5d891a_b314f0b3.displayName = "Box";
return Box_box_b2648d643be7668769c362a7ec5d891a_b314f0b3;
})();

export const Cond_comp_01115f5df92b892141762f15a1cfdd7e_b314f0b3 = /*#__PURE__*/ (() => {
const Cond_comp_01115f5df92b892141762f15a1cfdd7e_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        ((reflex___state____state__ai_study_canvas___home____state.level_rx_state_?.valueOf?.() === "College student"?.valueOf?.())?(children?.at?.(0)):(children?.at?.(1)))
    )
});
Cond_comp_01115f5df92b892141762f15a1cfdd7e_b314f0b3.displayName = "Cond";
return Cond_comp_01115f5df92b892141762f15a1cfdd7e_b314f0b3;
})();

export const Box_box_79b789337209896022db43b2a8ec6136_b314f0b3 = /*#__PURE__*/ (() => {
const Box_box_79b789337209896022db43b2a8ec6136_b314f0b3 = memo(({children, ...rest}) => {
    const on_click_16bf7d3c3886baba40054cf7e996551d = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ai_study_canvas___home____state.set_level", ({ ["value"] : "College student" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])
const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        jsx(RadixThemesBox,{...mergeSlotProps(rest, ({ css:({ ["cursor"] : "pointer", ["padding"] : "1rem 1.25rem", ["borderRadius"] : "12px", ["border"] : ((reflex___state____state__ai_study_canvas___home____state.level_rx_state_?.valueOf?.() === "College student"?.valueOf?.()) ? "1px solid #6366F1" : "1px solid rgba(255,255,255,0.08)"), ["background"] : ((reflex___state____state__ai_study_canvas___home____state.level_rx_state_?.valueOf?.() === "College student"?.valueOf?.()) ? "#6366F126" : "transparent"), ["boxShadow"] : ((reflex___state____state__ai_study_canvas___home____state.level_rx_state_?.valueOf?.() === "College student"?.valueOf?.()) ? "0 0 24px #6366F133" : "none"), ["width"] : "100%" }), onClick:on_click_16bf7d3c3886baba40054cf7e996551d }))},children)
    )
});
Box_box_79b789337209896022db43b2a8ec6136_b314f0b3.displayName = "Box";
return Box_box_79b789337209896022db43b2a8ec6136_b314f0b3;
})();

export const Cond_comp_ee3849b056de7730fa2b3b12666c7702_b314f0b3 = /*#__PURE__*/ (() => {
const Cond_comp_ee3849b056de7730fa2b3b12666c7702_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        ((reflex___state____state__ai_study_canvas___home____state.level_rx_state_?.valueOf?.() === "University student"?.valueOf?.())?(children?.at?.(0)):(children?.at?.(1)))
    )
});
Cond_comp_ee3849b056de7730fa2b3b12666c7702_b314f0b3.displayName = "Cond";
return Cond_comp_ee3849b056de7730fa2b3b12666c7702_b314f0b3;
})();

export const Box_box_928151a6566f0f73223b5de8686ba70c_b314f0b3 = /*#__PURE__*/ (() => {
const Box_box_928151a6566f0f73223b5de8686ba70c_b314f0b3 = memo(({children, ...rest}) => {
    const on_click_b071842e8ad0109aaf2a57c9eb12b812 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ai_study_canvas___home____state.set_level", ({ ["value"] : "University student" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])
const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        jsx(RadixThemesBox,{...mergeSlotProps(rest, ({ css:({ ["cursor"] : "pointer", ["padding"] : "1rem 1.25rem", ["borderRadius"] : "12px", ["border"] : ((reflex___state____state__ai_study_canvas___home____state.level_rx_state_?.valueOf?.() === "University student"?.valueOf?.()) ? "1px solid #6366F1" : "1px solid rgba(255,255,255,0.08)"), ["background"] : ((reflex___state____state__ai_study_canvas___home____state.level_rx_state_?.valueOf?.() === "University student"?.valueOf?.()) ? "#6366F126" : "transparent"), ["boxShadow"] : ((reflex___state____state__ai_study_canvas___home____state.level_rx_state_?.valueOf?.() === "University student"?.valueOf?.()) ? "0 0 24px #6366F133" : "none"), ["width"] : "100%" }), onClick:on_click_b071842e8ad0109aaf2a57c9eb12b812 }))},children)
    )
});
Box_box_928151a6566f0f73223b5de8686ba70c_b314f0b3.displayName = "Box";
return Box_box_928151a6566f0f73223b5de8686ba70c_b314f0b3;
})();

export const Styledupload_comp_b39f82ed9da4c0df8e1959975844bd7c_b314f0b3 = /*#__PURE__*/ (() => {
const Styledupload_comp_b39f82ed9da4c0df8e1959975844bd7c_b314f0b3 = memo(({children}) => {
    const ref_notes_upload = useRef(null); refs["ref_notes_upload"] = ref_notes_upload;
const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)
const [filesById, setFilesById] = useContext(UploadFilesContext);
const on_drop_ae6909f40c83f2fc8fecbd32f35394dd = useCallback(((_ev_0) => ((e => setFilesById(filesById => {
    const updatedFilesById = Object.assign({}, filesById);
    updatedFilesById["notes_upload"] = e;
    return updatedFilesById;
  })
    )(_ev_0))), [addEvents, ReflexEvent, filesById, setFilesById])
const on_drop_rejected_2fcedbdc0771e7617b4270e2d1ac8cc9 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("_call_function", ({ ["function"] : (() => (refs['__toast']?.["error"]("", ({ ["title"] : "Files not Accepted", ["description"] : _ev_0.map(((osizayzf) => (osizayzf?.["file"]?.["path"]+": "+osizayzf?.["errors"].map(((wnkiegyk) => wnkiegyk?.["message"])).join(", ")))).join("\n\n"), ["closeButton"] : true, ["style"] : ({ ["whiteSpace"] : "pre-line" }) })))), ["callback"] : null }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])
const { getRootProps: xdvxrcsn, getInputProps: udaxihhe, isDragActive: bacghqta} = useDropzone(({ ["accept"] : ({ ["image/png"] : [".png"], ["image/jpeg"] : [".jpg", ".jpeg", ".jfif"], ["application/pdf"] : [".pdf"] }), ["maxFiles"] : 3, ["multiple"] : true, ["disabled"] : reflex___state____state__ai_study_canvas___home____state.is_processing_rx_state_, ["id"] : "notes_upload", ["onDrop"] : on_drop_ae6909f40c83f2fc8fecbd32f35394dd, ["onDropRejected"] : on_drop_rejected_2fcedbdc0771e7617b4270e2d1ac8cc9 }));



    return(
        jsx(Fragment,{},jsx("div",{className:"rx-Upload",css:({ ["border"] : "1.5px dashed #6366F166", ["borderRadius"] : "14px", ["padding"] : "2.5rem 1rem", ["width"] : "100%", ["background"] : "transparent", ["cursor"] : "pointer", ["textAlign"] : "center" }),id:"notes_upload",ref:ref_notes_upload,...xdvxrcsn()},jsx("input",{type:"file",...udaxihhe()},),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"column",gap:"2"},jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "52px", ["height"] : "52px", ["borderRadius"] : "14px", ["background"] : "#6366F126", ["border"] : "1px solid #6366F155" })},jsx(LucideUpload,{css:({ ["color"] : "#E8EAF6" }),size:22},)),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#E8EAF6", ["fontWeight"] : "600" })},"Drop your notes here"),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#8B90A8" }),size:"2"},"or click to select up to 3 files at once"))))
    )
});
Styledupload_comp_b39f82ed9da4c0df8e1959975844bd7c_b314f0b3.displayName = "StyledUpload";
return Styledupload_comp_b39f82ed9da4c0df8e1959975844bd7c_b314f0b3;
})();

export const Foreach_comp_1bfdce59786fe4cb3495d4df71e59c81_b314f0b3 = /*#__PURE__*/ (() => {
const Foreach_comp_1bfdce59786fe4cb3495d4df71e59c81_b314f0b3 = memo(({children}) => {
    const [filesById, setFilesById] = useContext(UploadFilesContext);



    return(
        Array.prototype.map.call((filesById["notes_upload"] ? filesById["notes_upload"].map((f) => f.name) : []) ?? [],((f_rx_state_,index_55826f185b9e627cae4f9ed346b9c4d0)=>(jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["padding"] : "0.3rem 0.6rem", ["borderRadius"] : "6px", ["background"] : "rgba(255,255,255,0.05)" }),direction:"row",key:index_55826f185b9e627cae4f9ed346b9c4d0,gap:"2"},jsx(LucideImage,{css:({ ["color"] : "#22D3EE" }),size:16},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#E8EAF6" }),size:"2"},f_rx_state_)))))
    )
});
Foreach_comp_1bfdce59786fe4cb3495d4df71e59c81_b314f0b3.displayName = "Foreach";
return Foreach_comp_1bfdce59786fe4cb3495d4df71e59c81_b314f0b3;
})();

export const Cond_comp_0642161c003a94e9c6083bb29f747c99_b314f0b3 = /*#__PURE__*/ (() => {
const Cond_comp_0642161c003a94e9c6083bb29f747c99_b314f0b3 = memo(({children}) => {
    const [filesById, setFilesById] = useContext(UploadFilesContext);



    return(
        (((filesById["notes_upload"] ? filesById["notes_upload"].map((f) => f.name) : []).length > 0)?(children?.at?.(0)):(children?.at?.(1)))
    )
});
Cond_comp_0642161c003a94e9c6083bb29f747c99_b314f0b3.displayName = "Cond";
return Cond_comp_0642161c003a94e9c6083bb29f747c99_b314f0b3;
})();

export const Bare_comp_0034be4ba7142b67d60633898d7e7ff0_b314f0b3 = /*#__PURE__*/ (() => {
const Bare_comp_0034be4ba7142b67d60633898d7e7ff0_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        reflex___state____state__ai_study_canvas___home____state.level_rx_state_
    )
});
Bare_comp_0034be4ba7142b67d60633898d7e7ff0_b314f0b3.displayName = "Bare";
return Bare_comp_0034be4ba7142b67d60633898d7e7ff0_b314f0b3;
})();

export const Button_button_dbf8dd2d3b7ed001ec289c5e832dadd9_b314f0b3 = /*#__PURE__*/ (() => {
const Button_button_dbf8dd2d3b7ed001ec289c5e832dadd9_b314f0b3 = memo(({children, ...rest}) => {
    const [filesById, setFilesById] = useContext(UploadFilesContext);
const on_click_08b4fa2da73dbafec4a2050a47c0853f = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ai_study_canvas___home____state.handle_upload", ({ ["files"] : filesById?.["notes_upload"], ["upload_param_name"] : "files", ["upload_id"] : "notes_upload", ["extra_headers"] : ({  }) }), ({  }), "uploadFiles"))], [_e], ({  })))), [addEvents, ReflexEvent, filesById, setFilesById])
const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        jsx(RadixThemesButton,{...mergeSlotProps(rest, ({ css:({ ["background"] : "linear-gradient(135deg, #6366F1, #8B5CF6)", ["color"] : "white", ["cursor"] : "pointer", ["boxShadow"] : "0 8px 24px #6366F144", ["marginTop"] : "0.75rem" }), disabled:reflex___state____state__ai_study_canvas___home____state.is_processing_rx_state_, loading:reflex___state____state__ai_study_canvas___home____state.is_processing_rx_state_, onClick:on_click_08b4fa2da73dbafec4a2050a47c0853f, radius:"medium", size:"3" }))},children)
    )
});
Button_button_dbf8dd2d3b7ed001ec289c5e832dadd9_b314f0b3.displayName = "Button";
return Button_button_dbf8dd2d3b7ed001ec289c5e832dadd9_b314f0b3;
})();

export const Bare_comp_def91ce767e2f313c27a3ef269437fc5_b314f0b3 = /*#__PURE__*/ (() => {
const Bare_comp_def91ce767e2f313c27a3ef269437fc5_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        reflex___state____state__ai_study_canvas___home____state.loading_text_rx_state_
    )
});
Bare_comp_def91ce767e2f313c27a3ef269437fc5_b314f0b3.displayName = "Bare";
return Bare_comp_def91ce767e2f313c27a3ef269437fc5_b314f0b3;
})();

export const Bare_comp_ea6a2940b348622ab0531942b18867a3_b314f0b3 = /*#__PURE__*/ (() => {
const Bare_comp_ea6a2940b348622ab0531942b18867a3_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        reflex___state____state__ai_study_canvas___home____state.error_message_rx_state_
    )
});
Bare_comp_ea6a2940b348622ab0531942b18867a3_b314f0b3.displayName = "Bare";
return Bare_comp_ea6a2940b348622ab0531942b18867a3_b314f0b3;
})();

export const Cond_comp_a26edce6c7a0fdbe3e8753f0b85f5ec4_b314f0b3 = /*#__PURE__*/ (() => {
const Cond_comp_a26edce6c7a0fdbe3e8753f0b85f5ec4_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        (!((reflex___state____state__ai_study_canvas___home____state.error_message_rx_state_?.valueOf?.() === ""?.valueOf?.()))?(children?.at?.(0)):(children?.at?.(1)))
    )
});
Cond_comp_a26edce6c7a0fdbe3e8753f0b85f5ec4_b314f0b3.displayName = "Cond";
return Cond_comp_a26edce6c7a0fdbe3e8753f0b85f5ec4_b314f0b3;
})();

export const Cond_comp_7ea37579a5bc60d88fe39b3ae620de02_b314f0b3 = /*#__PURE__*/ (() => {
const Cond_comp_7ea37579a5bc60d88fe39b3ae620de02_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        (reflex___state____state__ai_study_canvas___home____state.is_processing_rx_state_?(children?.at?.(0)):(children?.at?.(1)))
    )
});
Cond_comp_7ea37579a5bc60d88fe39b3ae620de02_b314f0b3.displayName = "Cond";
return Cond_comp_7ea37579a5bc60d88fe39b3ae620de02_b314f0b3;
})();

export const Img_img_5500b722a44a01331e9d1d824e407c91_b314f0b3 = /*#__PURE__*/ (() => {
const Img_img_5500b722a44a01331e9d1d824e407c91_b314f0b3 = memo(({children, ...rest}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        jsx("img",{...mergeSlotProps(rest, ({ css:({ ["width"] : "100%", ["height"] : "100%", ["objectFit"] : "contain" }), src:reflex___state____state__ai_study_canvas___home____state.rendered_img_rx_state_ }))},)
    )
});
Img_img_5500b722a44a01331e9d1d824e407c91_b314f0b3.displayName = "Img";
return Img_img_5500b722a44a01331e9d1d824e407c91_b314f0b3;
})();

export const Cond_comp_8ccd06126e8fda2691c8b09a36792e23_b314f0b3 = /*#__PURE__*/ (() => {
const Cond_comp_8ccd06126e8fda2691c8b09a36792e23_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        (!((reflex___state____state__ai_study_canvas___home____state.rendered_img_rx_state_?.valueOf?.() === ""?.valueOf?.()))?(children?.at?.(0)):(children?.at?.(1)))
    )
});
Cond_comp_8ccd06126e8fda2691c8b09a36792e23_b314f0b3.displayName = "Cond";
return Cond_comp_8ccd06126e8fda2691c8b09a36792e23_b314f0b3;
})();

export const Bare_comp_b7383a5485e81850d2aa931dfeae6281_b314f0b3 = /*#__PURE__*/ (() => {
const Bare_comp_b7383a5485e81850d2aa931dfeae6281_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        (reflex___state____state__ai_study_canvas___home____state.show_notes_rx_state_ ? "Hide notes" : "Yes, make notes")
    )
});
Bare_comp_b7383a5485e81850d2aa931dfeae6281_b314f0b3.displayName = "Bare";
return Bare_comp_b7383a5485e81850d2aa931dfeae6281_b314f0b3;
})();

export const Button_button_278b21e60807b1eeafbd81fd24460683_b314f0b3 = /*#__PURE__*/ (() => {
const Button_button_278b21e60807b1eeafbd81fd24460683_b314f0b3 = memo(({children, ...rest}) => {
    const on_click_1a50e2f8dc181715463f5672b56a8628 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ai_study_canvas___home____state.toggle_notes", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])



    return(
        jsx(RadixThemesButton,{...mergeSlotProps(rest, ({ css:({ ["background"] : "linear-gradient(135deg, #6366F1, #8B5CF6)", ["color"] : "white", ["cursor"] : "pointer", ["boxShadow"] : "0 8px 24px #6366F144" }), onClick:on_click_1a50e2f8dc181715463f5672b56a8628, radius:"medium", size:"3" }))},children)
    )
});
Button_button_278b21e60807b1eeafbd81fd24460683_b314f0b3.displayName = "Button";
return Button_button_278b21e60807b1eeafbd81fd24460683_b314f0b3;
})();

export const Bare_comp_f205e8c91cc9cb2e611e82feef5d7df6_b314f0b3 = /*#__PURE__*/ (() => {
const Bare_comp_f205e8c91cc9cb2e611e82feef5d7df6_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        reflex___state____state__ai_study_canvas___home____state.topic_rx_state_
    )
});
Bare_comp_f205e8c91cc9cb2e611e82feef5d7df6_b314f0b3.displayName = "Bare";
return Bare_comp_f205e8c91cc9cb2e611e82feef5d7df6_b314f0b3;
})();

export const Foreach_comp_f51dd9748584e865b2d0b22506207c2b_b314f0b3 = /*#__PURE__*/ (() => {
const Foreach_comp_f51dd9748584e865b2d0b22506207c2b_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        Array.prototype.map.call(reflex___state____state__ai_study_canvas___home____state.notes_rx_state_ ?? [],((n_rx_state_,index_8a43351bd1aa25c252007dae01769b85)=>(jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",key:index_8a43351bd1aa25c252007dae01769b85,gap:"3"},jsx(LucideCheck,{css:({ ["color"] : "#34D399", ["flexShrink"] : "0", ["marginTop"] : "4px" }),size:16},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#E8EAF6", ["lineHeight"] : "1.6" }),size:"3"},n_rx_state_)))))
    )
});
Foreach_comp_f51dd9748584e865b2d0b22506207c2b_b314f0b3.displayName = "Foreach";
return Foreach_comp_f51dd9748584e865b2d0b22506207c2b_b314f0b3;
})();

export const Cond_comp_7df097ff8589ee3119302407f174f3da_b314f0b3 = /*#__PURE__*/ (() => {
const Cond_comp_7df097ff8589ee3119302407f174f3da_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        (reflex___state____state__ai_study_canvas___home____state.show_notes_rx_state_?(children?.at?.(0)):(children?.at?.(1)))
    )
});
Cond_comp_7df097ff8589ee3119302407f174f3da_b314f0b3.displayName = "Cond";
return Cond_comp_7df097ff8589ee3119302407f174f3da_b314f0b3;
})();

export const Bare_comp_0efab23c5416507ed3e8daf5e6f36259_b314f0b3 = /*#__PURE__*/ (() => {
const Bare_comp_0efab23c5416507ed3e8daf5e6f36259_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        (reflex___state____state__ai_study_canvas___home____state.show_quiz_rx_state_ ? "Regenerate quiz" : "Generate quiz")
    )
});
Bare_comp_0efab23c5416507ed3e8daf5e6f36259_b314f0b3.displayName = "Bare";
return Bare_comp_0efab23c5416507ed3e8daf5e6f36259_b314f0b3;
})();

export const Button_button_bea683b13f099da35eceb57118f1eba5_b314f0b3 = /*#__PURE__*/ (() => {
const Button_button_bea683b13f099da35eceb57118f1eba5_b314f0b3 = memo(({children, ...rest}) => {
    const on_click_a8f5f2e895a5377cbf1605ed5121b1b6 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ai_study_canvas___home____state.generate_quiz", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])



    return(
        jsx(RadixThemesButton,{...mergeSlotProps(rest, ({ css:({ ["background"] : "linear-gradient(135deg, #6366F1, #8B5CF6)", ["color"] : "white", ["cursor"] : "pointer", ["boxShadow"] : "0 8px 24px #6366F144" }), onClick:on_click_a8f5f2e895a5377cbf1605ed5121b1b6, radius:"medium", size:"3" }))},children)
    )
});
Button_button_bea683b13f099da35eceb57118f1eba5_b314f0b3.displayName = "Button";
return Button_button_bea683b13f099da35eceb57118f1eba5_b314f0b3;
})();

export const Foreach_comp_8816970d6cdf4f34b4d42640835c1a10_b314f0b3 = /*#__PURE__*/ (() => {
const Foreach_comp_8816970d6cdf4f34b4d42640835c1a10_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        Array.prototype.map.call(reflex___state____state__ai_study_canvas___home____state.ai_quiz_rx_state_ ?? [],((item_rx_state_,i_rx_state_)=>(jsx(RadixThemesBox,{css:({ ["paddingTop"] : "1.25rem", ["paddingBottom"] : "1.25rem", ["borderBottom"] : "1px solid rgba(255,255,255,0.08)", ["width"] : "100%" }),key:i_rx_state_},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#E8EAF6", ["fontWeight"] : "600" }),size:"4"},"Q",(i_rx_state_ + 1),". ",item_rx_state_?.["q"]),jsx(Fragment,{},(reflex___state____state__ai_study_canvas___home____state.submitted_rx_state_?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["paddingTop"] : "0.5rem", ["paddingLeft"] : "1rem", ["borderLeft"] : "2px solid #34D39944" }),direction:"column",gap:"1"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"3"},jsx(LucideCheck,{css:({ ["color"] : "#34D399" }),size:18},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#34D399", ["fontWeight"] : "600" }),size:"3"},item_rx_state_?.["answer"])),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#8B90A8", ["marginTop"] : "0.5rem" }),size:"2"},"Other options:"),Array.prototype.map.call(item_rx_state_?.["options"] ?? [],((opt_rx_state_,index_c94dc3bb9af2a10fa9a61d0a35b40a6d)=>(jsx(Fragment,{key:index_c94dc3bb9af2a10fa9a61d0a35b40a6d},(!((opt_rx_state_?.valueOf?.() === item_rx_state_?.["answer"]?.valueOf?.()))?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"3"},jsx(LucideDot,{css:({ ["color"] : "#8B90A8" }),size:16},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#8B90A8" }),size:"2"},opt_rx_state_)))):(jsx(Fragment,{},)))))))))):(jsx(Fragment,{},)))))))))
    )
});
Foreach_comp_8816970d6cdf4f34b4d42640835c1a10_b314f0b3.displayName = "Foreach";
return Foreach_comp_8816970d6cdf4f34b4d42640835c1a10_b314f0b3;
})();

export const Button_button_bcd01411497fc87cf647bc6c158d1e84_b314f0b3 = /*#__PURE__*/ (() => {
const Button_button_bcd01411497fc87cf647bc6c158d1e84_b314f0b3 = memo(({children, ...rest}) => {
    const on_click_4054014577629cc111fdffde9c6abbf5 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ai_study_canvas___home____state.reset_quiz", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])



    return(
        jsx(RadixThemesButton,{...mergeSlotProps(rest, ({ css:({ ["cursor"] : "pointer" }), onClick:on_click_4054014577629cc111fdffde9c6abbf5, size:"3", variant:"outline" }))},children)
    )
});
Button_button_bcd01411497fc87cf647bc6c158d1e84_b314f0b3.displayName = "Button";
return Button_button_bcd01411497fc87cf647bc6c158d1e84_b314f0b3;
})();

export const Button_button_1eddb0ad0291509b04c0253f626c3141_b314f0b3 = /*#__PURE__*/ (() => {
const Button_button_1eddb0ad0291509b04c0253f626c3141_b314f0b3 = memo(({children, ...rest}) => {
    const on_click_8631dd44dc46ff08e09cef311577ba01 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ai_study_canvas___home____state.check_quiz", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])



    return(
        jsx(RadixThemesButton,{...mergeSlotProps(rest, ({ css:({ ["background"] : "linear-gradient(135deg, #6366F1, #8B5CF6)", ["color"] : "white", ["cursor"] : "pointer", ["boxShadow"] : "0 8px 24px #6366F144" }), onClick:on_click_8631dd44dc46ff08e09cef311577ba01, radius:"medium", size:"3" }))},children)
    )
});
Button_button_1eddb0ad0291509b04c0253f626c3141_b314f0b3.displayName = "Button";
return Button_button_1eddb0ad0291509b04c0253f626c3141_b314f0b3;
})();

export const Cond_comp_fb05e430ff87222bbc52eaa0bd66c5e3_b314f0b3 = /*#__PURE__*/ (() => {
const Cond_comp_fb05e430ff87222bbc52eaa0bd66c5e3_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        (reflex___state____state__ai_study_canvas___home____state.submitted_rx_state_?(children?.at?.(0)):(children?.at?.(1)))
    )
});
Cond_comp_fb05e430ff87222bbc52eaa0bd66c5e3_b314f0b3.displayName = "Cond";
return Cond_comp_fb05e430ff87222bbc52eaa0bd66c5e3_b314f0b3;
})();

export const Cond_comp_c326409dca600da98f025bac0b0b3f4f_b314f0b3 = /*#__PURE__*/ (() => {
const Cond_comp_c326409dca600da98f025bac0b0b3f4f_b314f0b3 = memo(({children}) => {
    const reflex___state____state__ai_study_canvas___home____state = useContext(StateContexts.reflex___state____state__ai_study_canvas___home____state)



    return(
        (reflex___state____state__ai_study_canvas___home____state.show_quiz_rx_state_?(children?.at?.(0)):(children?.at?.(1)))
    )
});
Cond_comp_c326409dca600da98f025bac0b0b3f4f_b314f0b3.displayName = "Cond";
return Cond_comp_c326409dca600da98f025bac0b0b3f4f_b314f0b3;
})();
